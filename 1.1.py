import os


# path = input("Please enter the directory path to see files and subdirectories. ")
path = input("Enter the directory to see files and subdirectories: ")


def list_directory_contents(path):
    try:
        dir_list1 = os.scandir(path)
        print(f"Files within {path} are: ")
        for file in dir_list1:
            print(file)
    except FileNotFoundError:
        print("Path not found. Please try again.")
    except PermissionError:
        print("You do not have permission to access this file.")
    
    while True:
        again = input("Run again? (yes/no) ")
        if again.lower() == "yes":
            try:
                path = input("Enter the directory to see files and subdirectories: ")
                dir_list1 = os.listdir(path)
                print(f"Files within {path} are: ")
                for file  in dir_list1:
                    print(file)
            except FileNotFoundError:
                print("Path not found. Please try again.")
            except PermissionError:
                print("You do not have permission to access this file.")

        else:
            break

list_directory_contents(path)