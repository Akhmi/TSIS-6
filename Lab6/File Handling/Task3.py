import os

def find_filename_and_directory(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"The path '{path}' exists.")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")

path = "C:\PP2\Lab1\Python Exercises"

find_filename_and_directory(path)
