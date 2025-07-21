import os





print(os.getcwd())
# os.chdir("C:/WORK-DIR/code/LIVE/")
# print(os.getcwd())  # Output: Updated directory path
# os.mkdir("DAY_7")
print(os.listdir("."))
# os.makedirs("live")

print(os.path.exists("data.csv"))  # Output: True if file exists, else False
print(os.path.isfile("data.csv"))  # Output: True if it's a file
print(os.path.isdir("DAY_7s"))  # Output: True if it's a directory


os.environ["HOME"] = "PYTHONPATH"
print(os.getenv("HOME"))  # Output: value
print(os.getenv("HOME"))  # Output: Path of the user's home directory
print(os.environ)

os.system("dir")  # Lists all files and directories (Windows)

path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # Output: folder/subfolder/file.txt

print(os.name)
print(os.getpid())

import os

for file in os.listdir("."):
    if file.endswith(".py"):
        print(file)



