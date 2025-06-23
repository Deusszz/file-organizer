import os  # Provides functions for interacting with the operating system (like files and folders)
import shutil  # Provides high-level file operations (like moving files)
import argparse  # Helps parse command line arguments, so user can customize folder path
import json  # For reading the config.json file
import sys  # Allows graceful script exit
import logging # For logging events and errors to a file

# Configure logging settings
logging.basicConfig(
    filename='file_organizer.log', # Log file name
    filemode='a', # Append mode, so logs are added to the end of the file
    level=logging.INFO, # Log level (INFO and above)
    format='%asctime)s - %(levelname)s - %(message)s' # Log format with timestamp, level, and message
)

print("Starting file organizer...")  # Let the user know script started
logging.info("Started file organizer")  # Log the start of the script

# Dynamically get current user's Downloads folder path (Windows/macOS/Linux compatible)
default_downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Attempt to load config file and get folder_to_organize setting if present
config_path = "config.json"
config_folder = None  # Default if config or key not found
try:
    with open(config_path, "r") as config_file:
        config = json.load(config_file)  # Load the JSON config file
        config_folder = config.get("folder_to_organize", None)  # Get the folder path from config
        if config_folder:
            print(f"Loaded folder_to_organize from config: {config_folder}")
            logging.info(f"Loaded folder_to_ogranize from config: {config_folder}")
except FileNotFoundError:
    print(f"⚠️ {config_path} not found, using defaults")
    logging.warning(f"{config_path} not found, using defaults")  # Log missing config file
except json.JSONDecodeError:
    print(f"⚠️ {config_path} is not a valid JSON file, ignoring")
    logging.warning(f"{config_path} is not a valid JSON file, ignoring")  # Log invalid JSON

# Determine initial folder path from config if given, else default Downloads
if config_folder:
    # If config_folder is "Downloads", get the actual full Downloads path dynamically
    if config_folder.lower() == "downloads":
        folder_path_from_config = default_downloads_path
    else:
        # Otherwise, assume config_folder is a full path or relative folder name
        folder_path_from_config = os.path.expanduser(config_folder)
else:
    folder_path_from_config = default_downloads_path

# Set up argument parsing to allow user to specify folder path when running the script
parser = argparse.ArgumentParser(description="Organize files in a folder by file extension.")

# Add an optional argument --path to specify folder path (default is Downloads)
parser.add_argument(
    "--path",
    type=str,
    default=folder_path_from_config,  # Use config/default logic here
    help="Path to the folder to organize (default is your Downloads folder)"
)

# Parse the arguments from the command line
args = parser.parse_args()

# Final folder to organize (CLI arg > config > default)
downloads_path = args.path

# Validate that the path exists and is a directory
if not os.path.exists(downloads_path):
    print(f"❌ The specified path does not exist: {downloads_path}")
    logging.error(f"The specified path does not exist: {downloads_path}")
    sys.exit(1)
elif not os.path.isdir(downloads_path):
    print(f"❌ The path is not a folder: {downloads_path}")
    logging.error(f"The path is not a fodler: {downloads_path}")
    sys.exit(1)

print(f"Organizing files in: {downloads_path}")  # Inform user organizing is starting, showing the folder
logging.info(f"Organzing files in: {downloads_path}")  # Log the folder being organized

# Try the file organizing block
try:
    # Loop through everything inside the downloads_path folder
    for file_name in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file_name)  # Full path to the current file or folder

        print(f"Found: {file_name}")  # Show the current item found
        logging.info(f"Found: {file_name}")

        # Check if the current item is a folder/directory
        if os.path.isdir(file_path):
            print("⤵️ Skipping folder")  # We don't organize folders themselves, skip them
            logging.info(f"Skipped folder; {file_name}")
            continue  # Skip to next item

        # Extract the file extension, e.g. ".exe", ".zip" etc. Convert to lowercase
        file_ext = os.path.splitext(file_name)[1].lower()

        if file_ext:
            # Create folder name like "EXE_Files" by stripping the dot and converting to uppercase
            folder_name = file_ext[1:].upper() + "_Files"
        else:
            # If file has no extension, put it in "No_Extension" folder
            folder_name = "No_Extension"

        # Clean folder name to include only letters, numbers, underscore, dash, and space (to avoid weird names)
        folder_name = "".join(c for c in folder_name if c.isalnum() or c in "_- ")

        # Create the full path for the folder to move files into
        folder_path = os.path.join(downloads_path, folder_name)

        # Make the folder if it doesn't exist, but don't throw an error if it does
        os.makedirs(folder_path, exist_ok=True)

        try:
            # New path where the file will be moved
            new_file_path = os.path.join(folder_path, file_name)
            # Move the file into the folder
            shutil.move(file_path, new_file_path)
            print(f"✅ Moved {file_name} → {folder_name}")
            logging.info(f"Moved {file_name} to {folder_name}")  # Log successful move
        except Exception as e:
            # Catch any errors during move (e.g. file in use) and print an error message
            print(f"❌ Error moving {file_name}: {e}")
            logging.error(f"Error moving {file_name}: {e}")

except Exception as e:
    # Catch unexpected errors in the whole organizing block
    print(f"🔥 Unexpected error while organizing files: {e}")
    logging.critical(f"Unexpected error: {e}")  # Log critical error
    sys.exit(1)
