matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# matrix = [
#       C0  C1 C2
#  R0   [1, 2, 3],
#  R1   [4, 5, 6],
#  R2   [7, 8, 9]
# ]

# print(matrix[0])
# print(matrix[2][2])

# Printing each element of the matrix
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
# Output: 1 2 3 4 5 6 7 8 9

         #COLUMNS                       # ROWS
# grid = [[0 for _ in range(3)] for _ in range(4)]
# print(grid)
#
# transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transposed)

# numbers = [4, 2, 9, 1, 5]
# numbers.sort()  # In-place sorting
# print(numbers)  # Output: [1, 2, 4, 5, 9]
#
# new_list = sorted(numbers, reverse=False)  # Sort in descending order
# print(new_list)  # Output: [9, 5, 4, 2, 1]
#
# words = ["apple", "banana", "cherry", "date"]
# words.sort(key=len)
# print(words)

# HOW TO COPY ELEMENTS AND WHAT IS THE DIFFERENCE BETWEEN
 # DEEP COPY AND SHALLOW COPY

# original = [1, 2, 3]
# copy_list = original
# copy_list[0] = 99
# print(original)  # Output: [1, 2, 3]
# print(copy_list) # Output: [99, 2, 3]

# numbers = [10, 15, 20, 25, 30]
# filtered = [x for x in numbers if x % 20 == 0]
# print(filtered)

stack = []
stack.append(10)
stack.append(20)
print(stack)  # Output: [10, 20]


stack.pop(-1)  # Removes and returns the last element
print(stack) # Output: [10]


# queue = [1, 2, 3]
# queue.pop(0)  # Removes the first element
# print(queue)  # Output: [2, 3]

from collections import deque, Counter

# queue = deque([1, 2, 3])
# queue.append(4)  # Add to the end
# queue.popleft()  # Remove from the front
# print(queue)     # Output: deque([2, 3, 4])

# nested_list = [[1, 2, 3], [4, 5], [6]]
# flattened = [item for sublist in nested_list for item in sublist]
# print(flattened)  # Output: [1, 2, 3, 4, 5, 6]


# original = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(original))
# print(unique)  # Output: [1, 2, 3, 4, 5]


# numbers = [1, 2, 2, 3, 3, 3, 4]
# most_common = Counter(numbers).most_common(2)
# print(most_common)  # Output: 3



data = [1, 2, 3, 4, 5, 6, 7, 8]
chunk_size = 4
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
print(chunks)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8]]


names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

zipped = list(zip(names, scores))
print(zipped)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 95)]


import copy

nested_list = [[1, 2], [3, 4]]
deep_copy = copy.copy(nested_list)
deep_copy[0][0] = 99
print(nested_list)  # Output: [[1, 2], [3, 4]]
print(deep_copy)    # Output: [[99, 2], [3, 4]]