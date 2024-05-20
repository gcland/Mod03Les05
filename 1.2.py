import os

path = input("Enter the directory to see files and subdirectories: ")

def list_directory_contents(path):
    try:
        for item in os.scandir(path.lower()):
            if item.is_file():
                print(f"File: {item.name}")
                file_size = os.path.getsize(item)
                print(f"> [{item.name}] file size in Bytes is {file_size}")
            if item.is_dir():
                print(f"\nFolder: {item.name}")
                file_size = os.path.getsize(item)
                print(f"> [{item.name}] file size in Bytes is {file_size}")
                folder = item.name
                for subitem in os.scandir(item):
                    if subitem.is_file():
                        print(f"{folder} File: {subitem.name}")
                        file_size = os.path.getsize(subitem)
                        print(f"> [{subitem.name}] file size in Bytes is {file_size}")
        
    except FileNotFoundError:
        print("Path not found. Please try again.")
    except PermissionError:
        print("You do not have permission to access this file.")
    
    while True:
        again = input("Run again? (yes/no) ")
        if again.lower() == "yes":
            try:
                path = input("Enter the directory to see files and subdirectories: ")
                for item in os.scandir(path.lower()):
                    if item.is_file():
                        print(f"File: {item.name}")
                        file_size = os.path.getsize(item)
                        print(f"> [{item.name}] file size in Bytes is {file_size}")
                    if item.is_dir():
                        print(f"Folder: {item.name}")
                        file_size = os.path.getsize(item)
                        print(f"> [{item.name}] file size in Bytes is {file_size}")
                        folder = item.name
                        for subitem in os.scandir(item):
                            if subitem.is_file():
                                print(f"{folder} File: {subitem.name}")
                                file_size = os.path.getsize(subitem)
                                print(f"> {subitem.name} file size in Bytes is {file_size}")
            except FileNotFoundError:
                print("Path not found. Please try again.")
            except PermissionError:
                print("You do not have permission to access this file.")

        else:
            break

list_directory_contents(path)