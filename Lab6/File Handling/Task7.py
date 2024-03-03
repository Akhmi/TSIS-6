def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One or both files not found.")
    except IOError:
        print("Error copying files.")

source_file = "c:\KBTU\Programming principles\PP2\Some files\AnyList.txt"
destination_file = "c:\KBTU\Programming principles\PP2\Some files\Some.txt"

copy_file(source_file, destination_file)
