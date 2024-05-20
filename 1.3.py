import os

path = input("Enter the directory to see files and subdirectories: ")

def list_directory_contents(path):
    try:
        f = 0
        t = 0
        p = 0
        for item in os.scandir(path.lower()):
            if item.is_file():
                print(f"File: {item.name}")
                # file_size = os.path.getsize(item)
                # print(f"> File Size in Bytes is {file_size}")
                
                # this will return a tuple of root and extension
                split_tup = os.path.splitext(item)
                
                # extract the file name and extension
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
                    print("\nFile Extension: Folder", file_extension.lower())
                else:
                    print("\nFile Extension: ", file_extension.lower())
                
            if item.is_dir():
                print(f"\nFolder: {item.name}")
                # file_size = os.path.getsize(item)
                # print(f"> File Size in Bytes is {file_size}")
                folder = item.name
                
                # this will return a tuple of root and extension
                split_tup = os.path.splitext(item)
             
                # extract the file name and extension
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
                    print("\nFile Extension: Folder", file_extension.lower())
                else:
                    print("\nFile Extension: ", file_extension.lower())

                for subitem in os.scandir(item):
                    if subitem.is_file():
                        print(f"{folder} File: {subitem.name}")
                        # file_size = os.path.getsize(item)
                        # print(f"> File Size in Bytes is {file_size}")

                        # this will return a tuple of root and extension
                        split_tup = os.path.splitext(item)
                        
                        # extract the file name and extension
                        file_name = split_tup[0]
                        file_extension = split_tup[1]
                        if file_extension.lower() == ".txt":
                            t+=1
                        if file_extension.lower() == ".py":
                            p+=1
                        if file_extension.lower() == "":
                            f+=1
                        
                        print("File Name: ", file_name.lower())
                        print(split_tup)
                        if file_extension == "":
                            print("\nFile Extension: Folder", file_extension.lower())
                        else:
                            print("\nFile Extension: ", file_extension.lower())
        print(f)
        print(t)
        print(p)
    except FileNotFoundError:
        print("Path not found. Please try again.")
    except PermissionError:
        print("You do not have permission to access this file.")

list_directory_contents(path)

