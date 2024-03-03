import os

def check_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    if os.access(path, os.R_OK):
        print(f"Read access to '{path}' is allowed.")
    else:
        print(f"Read access to '{path}' is not allowed.")

    if os.access(path, os.W_OK):
        print(f"Write access to '{path}' is allowed.")
    else:
        print(f"Write access to '{path}' is not allowed.")

    if os.name == 'posix':
        if os.access(path, os.X_OK):
            print(f"Execute access to '{path}' is allowed.")
        else:
            print(f"Execute access to '{path}' is not allowed.")

path = "C:\PP2\Lab1\Python Exercises"

check_access(path)
