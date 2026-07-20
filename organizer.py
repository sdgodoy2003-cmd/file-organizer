from pathlib import Path
import shutil

file_types = {
    "Image":[".jpg",".png",".gif"],
    "Video":[".mp4",".mkv"],
    "Audio":[".mp3",".wav"],
    "Document":[".pdf",".txt",".docx"],
    "Code":[".py",".js",".java",".cpp",".html",".css"],
    "Executables":[".exe",".app",".sh"],
    "Compressed":[".zip",".rar",".7z"]
}

def get_file_type(file):
    extension = file.suffix
    
    for category, extensions in file_types.items():
        if extension in extensions:
            return category
    return "Others"

def analyze_folder(directory):
    elements = directory.iterdir()
    organized_files = {}
    for element in elements:
            if element.is_file():
                category = get_file_type(element)
                if category in organized_files:
                    organized_files[category].append(element)
                else:
                    organized_files[category] = [element]
    return organized_files

def create_folders(organized_files, directory):
    for category in organized_files:
        folder_path = directory / category
        folder_path.mkdir(exist_ok=True)

def move_files(organized_files, directory):
    for category, files in organized_files.items():
        destination = directory / category
        for file in files:
            shutil.move(file, destination)