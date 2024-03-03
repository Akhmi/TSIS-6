def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in '{filename}' is: {line_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except IOError:
        print(f"Error reading file '{filename}'.")

filename = "c:\KBTU\Programming principles\PP2\Some files\Әнұран.txt"

count_lines(filename)