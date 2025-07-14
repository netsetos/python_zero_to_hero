# person = {"name": "Alice",
#           "age": 25,
#         "city": "New York"}
# item = person.popitem()
# print(item)
# del person["age"]
# print(person)

# age = person.pop("age")
# print(age)
# # if age > 18:
# #     print("VOTE")
# # print(person)
#
# # Using popitem() (removes and returns the last inserted pair in Python 3.7+)
# item = person.popitem()
# print(item)  # Output: ( "city": "New York")
#
# person.clear()
# print(person)

person = {"name": "Alice", "age": 25, "city": "New York"}
# print(person.keys())
# print(person.values())
# print(person.items())

# Iterating Over a Dictionary

# for key in person:
#     print(key)

# for value in person.values():
#     print(value)

# for key,value in person.items():
#     print(f"{key},{value}")

students = {
    "student1": {"name": "Alice", "age": 22},
    "student2": {"name": "Bhanu", "age": 21}
}

# print(students["student2"]["name"])


# # Squaring numbers using dictionary comprehension
# squares = {x**2: x**4 for x in range(5)}
# print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering dictionary items
original = {"a": 1, "b": 2, "c": 3}
filtered = {k: v for k, v in original.items() if v > 1}
print(filtered)  # Output: {'b': 2, 'c': 3}




















