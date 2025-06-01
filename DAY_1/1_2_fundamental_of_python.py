#Example: Mutable Object (List)

my_list = [1, 2, 3]
my_list[0] = 10  # Modifies the first element
print(my_list)   # Output: [10, 2, 3]


#Example: Immutable Object (String)
my_string = "hello"
my_string[0] = 'H'  # This will raise an error

# Instead, create a new string:
new_string = "H" + my_string[1:]
print(new_string)  # Output: "Hello"