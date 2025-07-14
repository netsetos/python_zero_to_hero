#
# string3 = '''This is a multi-line string.
# This is a multi-line string.
# This is a multi-line string.'''  #docstring
# # print(string3)
#
# def add(a,b):
#     '''
#
#     :param a:
#     :param b:
#     :return:
#     '''
#     c=a+b
#     return c
#
# addition=add("1","2")
# # print(addition)
#
#
# repeat = "Ha " *3
# print(repeat)

# text = "Hello-Python!"
# alpha=["a", "b", "c"]
# print("%".join(alpha))

# text = "Hello Python"
# vowels = "aeiouAEIOU"
# count = sum(1 for char in text if char in vowels)
# print(count)





# s=0
# for char in text:
#     if char in vowels:
#         s=s+1
# print(s)


# text =(1,2,3)
# text[0]=6
# print(text)





# for code in range(65, 91):  # Unicode for A-Z
#     print(chr(code), end=" ")


# words = ["Python", "is", "fun"]
result = "&".join(["Python", "is", "fun"])
# print(result)

names = ("Alice", "Bob", "Charlie")
result = ",".join(names)
# print(result)


items = [1, 2, 3, 4]
# Convert to strings first
result = "-".join(map(str, items))
# print(result)


original = "Python-is-fun"
parts = original.split("-")
joined = "-".join(parts)
# print("After split function, we got output in joined",joined)


name = "Aman"
age = 40
message = f"My name is {name} and I am {age} years old."

# print(message)


x=200
y=10
# z=x+y
result = f"The sum of {x} and {y} is {x * y}."
# print(result)


pi = 3.14159
formatted = f"Pi to 2 decimal places: {pi:.3f}"
# print(formatted)


name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
# print(message)

message = ("My name is {0} and I am {1} years old. and her sister is also {0}. and her age is also {1}"
           .format("Alice", 25))
# print(message)

pi = 3.14159
formatted = "Pi to 2 decimal places: {:.2f}".format(pi)
print(formatted)






