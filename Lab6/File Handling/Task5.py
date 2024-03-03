def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except IOError:
        print(f"Error writing to file '{filename}'.")

# Specify the filename and list data here
filename = "c:\KBTU\Programming principles\PP2\Some files\AnyList.txt"
data_list = ['March', 'April', 'May', 'June']

write_list_to_file(filename, data_list)
