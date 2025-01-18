import os

# get the current working directory
# print("__current working directory__", os.getcwd())


# change the working directory
def current_dir():
    print("__CWD__:", os.getcwd())
    print()
    
# current_dir()
# os.chdir("../../")
# current_dir()

# listing the files and directories
path = "/"
dir_list = os.listdir(path)
# print(f"files and directories in {path} are: {dir_list}")

# 
print(os.name)
print(os.error)