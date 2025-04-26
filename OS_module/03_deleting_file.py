import os

# **********************************************************************

# os.remove() -> removes a file not directory
# os.rmdir() -> remove an empty directory

file_path = "C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder/folder/test/test.txt"
non_empty_folder_path = "C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder/folder/test"
empty_folder_path = "C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder2/testFolder1/folder/test"

# os.remove(non_empty_folder_path)
# PermissionError: [WinError 5] Access is denied:

# os.remove(empty_folder_path)
# PermissionError: [WinError 5] Access is denied:

os.remove(file_path)

# os.rmdir(file_path)
# NotADirectoryError: [WinError 267] The directory name is invalid:

# os.rmdir(non_empty_folder_path)
# OSError: [WinError 145] The directory is not empty:

os.rmdir(empty_folder_path)