# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

#
# with open("example.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)

## Writing to a File
# with open("example.txt", "w") as file:
#     file.write("This is a new file.\n")
#     file.write("Python is fun!\n")
#     file.write("Pranav Learning is Fun")


# with open("example.txt", "w") as file:
#     file.writelines(["Line 1\n\t", "Line 2\n\n\t", "Line 3\n\t"])

# with open("example.txt", "a") as file:
#     file.write("\nThis line is appended. extra ")
#     file.write("\n This is a binus line we will learn gcp today ")


# file = open("example1.txt", "r")
# content = file.read()
# print(content)
# file.close()



# import os
#
# if os.path.exists("example1.txt"):
#     file = open("example1.txt", "r")
#     content = file.read()
#     print(content)
#     file.close()
# else:
#     print("File does not exist.")

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted.")
else:
    print("File not found.")


#File Closing


