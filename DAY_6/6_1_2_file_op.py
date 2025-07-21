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

# import os
#
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("File deleted.")
# else:
#     print("File not found.")


#File Closing

#1. Copying File Content
# with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
#     dest.write(src.read())

# with open("example.txt", "r") as file:
#     content = file.read()  # TO READ A FILE
#     print(content)
#     lines = content.split("\n")  # SPLIT is DOING EVERY LINE TO ELEMENT OF ARRAY
#     print(lines)
#     words = content.split()
#     print(words)
#     print(f"Lines: {len(lines)}, Words: {len(words)}, Characters: {len(content)}")



# try:
#     with open("example1.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file does not exist in our environment please check in folder 2")

# with open("python_bootcamp.png", "rb") as file:
#     binary_data = file.read()
#     print(binary_data[:100])  # Print first 20 bytes




with open("example.txt", "r") as file:
    file.seek(100)  # Move to the 10th byte
    print(file.read())  # Read from the 10th byte onward
    print("Cursor Position:", file.tell())  # Get the current position

