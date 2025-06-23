# File Organizer

A simple Python script to automatically organize your Downloads folder by file type, moving files into categorized folders like ZIP_Files, EXE_Files, JAR_Files, and more.

## Features

- Organizes files based on their extensions.
- Creates folders if they don't exist.
- Skips existing folders to avoid infinite loops.
- Handles errors like files being in use gracefully.
- Logs actions and errors to a 'file_organizer.log' file (can be ignored via '.gitignore').

  ## Installation

  Make sure you have Python installed (version 3.6 or higher recommended).

  Clone this repository:

  ```bash
  git clone https://github.com/Deusszz/file-organizer.git
  cd file-organizer
  ```

  ## Usage

  Run the script to organize your Downloads folder:
  ```bash
  python main.py
  ```
  You can also specify a custom folder path:
  ```bash
  python main.py --path "C://path/to/your/folder"
  ```

  ## Requirements

  - Python 3.6+
  - No additional packages required (uses only standard library)

  ## Logging

  The script generates a file_organizer.log file recording operations and errors.
  This log file is included in .gitignore by default to avoid committing it to the repository.
 
  ## Contributing

  Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

  ## License

  This project is licensed under the MIT License

  ## Why I made this

  This project is my first "real project" in an attempt to break into the tech space with hopes to eventually do freelance work
  
