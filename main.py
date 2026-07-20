from pathlib import Path
from organizer import analyze_folder, move_files, create_folders

def main():
    while True:
        user_path = input("Which directory do you want to organize?: ")
        path = Path(user_path)

        if path.is_dir():
            break

        print("\nInvalid directory, please try again.\n")


    organized_files = analyze_folder(path)
    print("\nFolder analyzed successfully.\n\nSummary:\n----------------")
    for category, files in organized_files.items():
        print(category.ljust(12),":", len(files))
    print("----------------\n")

    while True:
        confirmation = input("Do you want to continue? (y/n): ").lower()
        if confirmation == "y":
            create_folders(organized_files, path)
            move_files(organized_files, path)
            print("\nFolder organized successfully.")
            break
        elif confirmation == "n":
            print("\nNo changes were made.")
            break
        else:
            print("\nInvalid answer, please try again.\n")

if __name__ == "__main__":
    main()