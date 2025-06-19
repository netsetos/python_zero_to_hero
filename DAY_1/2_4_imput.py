# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# age = int(input("Enter your age: "))  # Convert string to int
# print("You will be", age + 1, "next year.")

#
# x, y = input("Enter two numbers: ").split()
# print("First number:", x)
# print("Second number:", y)
# print(x+y)

# x, y = map(int, input("Enter two numbers: ").split())
# print(x+y)




# print("Hello, World!")
#
# print("Python", "is", "awesome", sep="@")

# print("Hello", end="\t")  # Print without a newline
# print("World!")          # Output: Hello World!

# name = "Alice"
# age = 25
# print(f"{name} is {age} years old.")  # Output: Alice is 25 years old.
#
# print("My name is {} and I am {} years old.".format("Bob", 30))

# Program to calculate the area of a rectangle
# length = float(input("Enter the length: "))  # Accept length
# width = float(input("Enter the width: "))    # Accept width
#
# area = length * width  # Calculate area
# print(f"The area of the rectangle is {area:.2f}.")  # Print formatted result

print("Enter numbers line by line, and type 'done' to finish:")
numbers = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    numbers.append(int(line))

print("Sum of numbers:", sum(numbers))

# with open("output.txt", "w") as file:
#     print("This will be written to a file.", file=file)





