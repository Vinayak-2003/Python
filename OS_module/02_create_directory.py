import os


# ********************************************* os.mkdir() ***********************************************
# parent_dir = "C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder"

# directory = "testFolder"
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# print("directory '%s' created." %directory)

# directory = "testFolder2"
# mode = 0o666
# path = os.path.join(parent_dir, directory)
# os.mkdir(path, mode)
# print("directory '%s' created." %directory)

# directory = "test"
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# print("directory '%s' created." %directory)

# Traceback (most recent call last):
#   File "c:\Users\VinayakKanchan\Desktop\Programming\Python\OS_module\02_create_directory.py", line 18, in <module>
#     os.mkdir(path)
# FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder/folder\\test'


# ********************************************* os.makedirs() ***********************************************

# It is used to create a directory recursively. That means while making leaf directory if any 
# intermediate-level directory is missing, os.makedirs() method will create them all.

parent_dir = "C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder/folder"
directory = "test"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print(f"directory {directory} created")

parent_dir = "C:/Users/VinayakKanchan/Desktop/Programming/Python/testFolder2/testFolder1/folder"
directory = "test"
path = os.path.join(parent_dir, directory)
mode = 0o666
os.makedirs(path, mode)
print(f"directory {directory} created")