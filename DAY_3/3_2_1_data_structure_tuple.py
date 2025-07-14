# empty_tuple = ()
# print(empty_tuple)
#
# single_element = (42,)
# print(single_element)
#
# mixed_tuple = (1, "Hello", 3.14, True,"NETSETOS","LIVE CLASSES")
# print(mixed_tuple)
#
#
# tuple_without_parentheses = 1, 2, 3
# print(tuple_without_parentheses)

# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple[-1])

# my_tuple = (10, 20, 30, 40, 50)
#           #  0   1   2  3   4
# print(my_tuple[1:4])  # 20 30 40
# print(my_tuple[:3])   # Output: (10, 20, 30)
# print(my_tuple[3:])   # Output: (40, 50)
# print(my_tuple[::2])  # Output: (10, 30, 50) (every second element)

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# combined = tuple1 + tuple2
# print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# my_tuple = (1, 2)
# repeated = my_tuple * 3
# print(repeated)  # Output: (1, 2, 1, 2, 1, 2)

# my_tuple = ("apple", "banana", "cherry")`
# print("guava" not in my_tuple)

# my_tuple = (1, 2, 3, 4)
# my_tuple[0]=90
# print(my_tuple)
# TUPLE IS IMMUTABLE THATS WHY WE ARE NOT ABLE TO
# CHANGE THE VALUE

# my_tuple = (1, [2, 3], 4)
#
# # Changing the list inside the tuple
# my_tuple[1][0] = 99
# print(my_tuple)  # Output: (1, [99, 3], 4)

# my_tuple = (10, 20, 10, 30)
# print(my_tuple.count(10))
#
# print(my_tuple.index(30))

# packed_tuple = 1, "Hello", 3.14
# a,b,c=packed_tuple
# print(a)
# print(b)
# print(c)



# coordinates = {(10, 20): "Point A",
#                (30, 40): "Point B"}
# print(coordinates[(30, 40)])  # Output: Point A

#Real-World Use Cases
# def get_student_details():
#     return "Alice", 20, "Computer Science"
#
# name, age, course = get_student_details()
# print(name)   # Output: Alice
# print(age)    # Output: 20
# print(course) # Output: Computer Science

# a, b = 10, 20
# a, b = b, a
# print(a, b)  # Output: 20, 10

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days)


