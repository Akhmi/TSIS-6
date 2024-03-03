import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"The file '{path}' does not exist.")
        return

    if not os.access(path, os.W_OK):
        print(f"No write access to '{path}'. Cannot delete the file.")
        return

    try:
        os.remove(path)
        print(f"The file '{path}' has been successfully deleted.")
    except OSError as e:
        print(f"Error: {e.strerror}")

path_to_delete = "c:\KBTU\Programming principles\PP2\Some files\ForDelete.txt"

delete_file(path_to_delete)