#Examples of arithmetic operations in Python:
# Arithmetic Operators
a = 10
b = 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor Division: 3
print(a % b)    # Modulus: 1
print(a ** b)   # Exponentiation: 10^3 = 1000

# 2. Assignment Operators

# Assignment Operators
x = 5
print(x)        # Assign: 5

x += 2
print(x)        # Add and Assign: 7

x *= 3
print(x)        # Multiply and Assign: 21

x %= 4
print(x)        # Modulus and Assign: 1


# 3. Comparison Operators
# Examples of comparison operators:

# Comparison Operators
x = 10
y = 20

print(x == y)   # Equal to: Falsenetsetostech
print(x != y)   # Not Equal to: True
print(x > y)    # Greater than: False
print(x < y)    # Less than: True
print(x >= 10)  # Greater than or equal: True
print(x <= 5)   # Less than or equal: False


# 6. Membership Operators
# Membership Operators
my_list = [1, 2, 3, 4]
my_string = "Python"

print(2 in my_list)       # True (2 is in the list)
print(5 not in my_list)   # True (5 is not in the list)
print('P' in my_string)   # True ('P' is in the string)
print('z' not in my_string) # True ('z' is not in the string)

#Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)       # True (x and z point to the same object)
print(x is y)       # False (x and y are different objects, even if their content is the same)
print(x == y)       # True (x and y have the same content)
print(x is not y)   # True (x and y are not the same object)