# This is day 4 of my python series
'''
This is a sum function
It is used average the products
on site.
'''
if True:
    print("Hello, World!")  # Indented block
    print("here")


def factorial(n):
    # Base case for recursion
    if n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Calculate the factorial of 5
result = factorial(5)
print(result)  # Output: 120










