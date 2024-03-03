import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        elif os.path.isfile(item_path):
            files.append(item)
        all_directories_files.append(item)

    print("Directories:")
    print(directories)
    print("\nFiles:")
    print(files)
    print("\nAll Directories/Files:")
    print(all_directories_files)

path = "C:\PP2\Lab5\Lab5"

list_directories_files(path)