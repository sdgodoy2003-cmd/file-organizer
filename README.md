# File Organizer

## About

A command-line application that analyzes a user-selected directory, categorizes files based on their type, and automatically organizes them into folders. Before making any changes, it displays a summary of the detected files and asks the user for confirmation.

## Features

- Analyzes a user-selected directory and detects its files.
- Categorizes files based on their extensions.
- Creates folders automatically according to each file category.
- Moves files into their corresponding folders.
- Shows a summary of the detected files before making changes.
- Asks for user confirmation before organizing files.

## Technical Details

- Uses `pathlib` for filesystem navigation.
- Uses `shutil` to move files.
- Uses dictionaries to map file extensions to categories.
- Built with a modular structure separating user interaction and file organization logic.

## Technologies

- Python 3
- pathlib (filesystem navigation and path handling)
- shutil (file operations such as moving files)

## How to Run

No additional dependencies are required.

1. Clone this repository:

```bash
git clone https://github.com/sdgodoy2003-cmd/file-organizer.git
```

2. Navigate to the project folder:

```bash
cd file-organizer
```

3. Run the application:

```bash
python main.py
```

4. Enter the directory path you want to organize and confirm the operation when prompted.

## Example

```text
Which directory do you want to organize?: C:\Users\test  

Folder analyzed successfully.

Summary:
----------------
Image        : 5
Others       : 5
Document     : 3
Video        : 2
----------------

Do you want to continue? (y/n): y

Folder organized successfully.
```

## Future Improvements

- Add support for more file extensions.
- Add a graphical user interface.
- Add recursive folder organization.
- Allow users to customize file categories.