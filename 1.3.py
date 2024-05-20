import os

path = input("Enter the directory to see files and subdirectories: ")

def list_directory_contents(path):
    try:
        f = 0
        t = 0
        p = 0
        for item in os.scandir(path.lower()):
            if item.is_file():
                print(f"\nFile: {item.name}")
                file_size = os.path.getsize(item)
                print(f"> [{item.name}] file size in Bytes is {file_size}")
                
                split_tup = os.path.splitext(item)

                file_name = split_tup[0]
                file_extension = split_tup[1]
                if file_extension.lower() == ".txt":
                    t+=1
                if file_extension.lower() == ".py":
                    p+=1
                if file_extension.lower() == "":
                    f+=1
                print("File Name: ", file_name.lower())
                if file_extension == "":
                    print("File Extension: Folder", file_extension.lower())
                else:
                    print("File Extension: ", file_extension.lower())
                
            if item.is_dir():
                print(f"\nFolder: {item.name}")
                file_size = os.path.getsize(item)
                print(f"> [{item.name}] file size in Bytes is {file_size}")
                folder = item.name
                
                split_tup = os.path.splitext(item)
             
                file_name = split_tup[0]
                file_extension = split_tup[1]
                if file_extension.lower() == "":
                    f+=1
                
                print("File Name: ", file_name.lower())
                if file_extension == "":
                    print("File Extension: Folder", file_extension.lower())
                else:
                    print("File Extension: ", file_extension.lower())

                for subitem in os.scandir(item):
                    if subitem.is_file():
                        print(f"\n{folder} File: {subitem.name}")
                        file_size = os.path.getsize(subitem)
                        print(f"> [{subitem.name}] file size in Bytes is {file_size}")

                        split_tup = os.path.splitext(subitem)
                        
                        file_name = split_tup[0].lower()
                        file_extension = split_tup[1].lower()
                        if file_extension.lower() == ".txt":
                            t+=1
                        if file_extension.lower() == ".py":
                            p+=1

                        print("File Name: ", file_name.lower())
                        if file_extension == "":
                            print("File Extension: Folder", file_extension.lower())
                        else:
                            print("File Extension: ", file_extension.lower())

        print(f"\nFolders: {f}")
        print(f"Text files: {t}")
        print(f"Python files: {p}")

    except FileNotFoundError:
        print("Path not found. Please try again.")
    except PermissionError:
        print("You do not have permission to access this file.")
    finally:
        print("\nThanks for using this function!")
list_directory_contents(path)

