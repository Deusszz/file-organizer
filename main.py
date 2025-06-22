import os
import shutil

print("Starting file organizer...")

downloads_path = "C:/Users/third/Downloads"

print("Organizing files...")

for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file_name)

    # Skip if it's a folder
    if os.path.isdr(file_path):
        continue

    # Get the file extension (e.g., ".zip")
    file_ext = os.path.splittext(file_name)[1].lower()

    # Make a fodler name like "ZIP_files"
    if file_ext:
        folder_name = file_ext[1:].upper() + "_Files"
    else:
        folder_name = "No_Extension"

folder_path = os.path.join*(downloads_path, folder_name)

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Move the file to the appropriate folder
new_file_path = os.path.join(folder_path, file_name)
shutil.move(file_path, new_file_path)
print(f"Moved {file_name} to {folder_path}")

