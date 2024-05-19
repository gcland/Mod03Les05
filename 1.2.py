import os

file_path = 'folderB'

try:
    file_size = os.path.getsize(file_path)
    print(f"File Size in Bytes is {file_size}")
except FileNotFoundError:
    print("File not found.")
except OSError:
    print("OS error occurred.")