#Task 1: Directory Inspector:

#Problem Statement: Create a Python script that lists all files and subdirectories 
# in a given directory. Your script should prompt the user for the directory 
# path and then display the contents.

#Code Example:
import os

    
def list_directory_contents(path):
    try:
        files = []
        directories = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                files.append(item)
            elif os.path.isdir(item_path):
                directories.append(item)
        return {"Files": files, "Directories": directories}
    except FileNotFoundError:
        return f"Error: The File '{path}' does not exist."
    except PermissionError:
        return f"Error: Permission denied for accessing '{path}'. "

if __name__ == "__main__":
    file = "content.txt"
    content = "This is a text."
choice = input("Directory: ")
print(list_directory_contents(choice))

# List and print all files and subdirectories in the given path

#Expected Outcome: The script should correctly list all files 
# and subdirectories in the specified directory. Handle exceptions 
# for invalid paths or inaccessible directories.