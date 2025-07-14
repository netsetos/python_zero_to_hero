# def function_name():
#     print("This is a new function")
#     print("Welcome to Netsetos")
#     return 1+2
#
# # def greet(name):
# #     print(f"Welcome {name} to NETSETOS Python and DSA")
# #
# # print(greet("Tanu"))
#
# # Types of Functions
# # BUILT IN FUNCTIONS
# # User-Defined Functions
# def add_numbers(a, b):
#     return a + b
#
# print(add_numbers(3, 5))
#
#
# def multi_numbers(a, b):
#     return a * b
#
#
# print(multi_numbers(4, 5))
# # Output: 8
#
# # Anonymous Functions (Lambda Functions)
#
# cube = lambda x: x ** 3
# print(cube(9))  # Output: 16
#
#
# # def square(x):
# #     return x**x
#
# # Function Parameters
# #a) Positional Arguments
#
# def multiply(num1, num2,num3):
#     return num1 * num2 * num3
#
# print(multiply(2, 3,4))  # Output: 24
#
# def introduce(age,name):
#     return f"My name is {name} and I am {age} years old."
#
# print(introduce(name="Bob" , age=25 ))
# # Output: My name is Bob and I am 25 years old.


# d) Variable-Length Arguments
# def sum_all(*num):
# #     return sum(num)
# #
# # print(sum_all(1,2,3,5,6,7,1,2,3,5,6,7))

# Keywords Length Arguments

def print_details(**details):
    for key,value in details.items():
        print(f"Key is {key} and value is {value}" )


# print_details(name="Atul", age=18)

# Return statement
# def subtract(a, b):
#     return a - b
#
# result = subtract(10, 4)
# print(result)  # Output: 6


# a) Local Scope
def example():
    x = 5  # Local variable
    print(x+2)

# example()
# print(x)  # Error: x is not defined

# # b) Global Scope
# y = 10  # Global variable
# def show():
#     print(y)
# show()  # Output: 10

# z = 20   # Global variable
# def modify():
#     global z
#     z += 5
# modify()
# print(z)  # Output: 25


# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     inner_function()
#
# outer_function("Hello from the inner function!")
# Output: Hello from the inner function!

# def decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper
#
# @decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

# def factorial(n):  # 5
#     if n == 1:     #5==1  4==1 3==1 2==1
#         return 1
#     return n * factorial(n - 1)    # 5 *   4   *  3 *  2 * 1 --
#
# print(factorial(5))  # Output: 120   5*4*3*2*1  = 120




# 4. Local and Global with Same Name

# a = 5  # Global variable
#
# def my_function():
#     a = 10  # Local variable
#     print("Local variable a:", a)  # What get printed 10
#
# my_function()
# print("Global variable a:", a)  # what will get printed  5


# def outer_function():
#     x = 5  # Enclosing variable
#
#     def inner_function():
#         nonlocal x
#         x += 1
#         print("Inner function x:", x)
#
#     inner_function()
#     print("Outer function x:", x)


# def example(a, b=10, /, c=20, *args, d, **kwargs):
#     print(f"a: {a}, b: {b}, c: {c}, args: {args}, d: {d}, kwargs: {kwargs}")
#
# example(5, 15, 25, 30, 35, d=50, e=60, f=70)




# Example with a list
# fruits = ["apple", "banana", "cherry"] # 0 but if you want to change the numbering from one than
# # for index, fruit in enumerate(fruits, start=1):
# #     print(index, fruit)
# # # Output:
# # # 1 apple
# # # 2 banana
# # # 3 cherry
# #
# # # Example converting to a list
# # print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# result = divmod(10, 3)
# print(result)


# seconds = 2500
# minutes, seconds = divmod(seconds, 60)
# print(minutes, seconds)


my_list = [1, 2, 3]
print(dir(my_list))

import math
print(dir(math))
# Output (partial): ['acos', 'asin', 'atan', 'ceil', ...]























