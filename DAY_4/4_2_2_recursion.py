







# def recursive_function(parameters):
#     if base_case_condition:
#         return base_case_value
#     else:
#         return recursive_function(smaller_parameters)


# BASE CONDITION IS VERY MUCH COMPULSARY IN RECURSIVE
# TO STOP THE PROGRAM FROM INFINITE LOOP


# def fact(n):      # fact(0)
#     if n == 0:  # Base case # 2==0
#         return 1
#     else:  # Recursive case
#         return n * fact(n - 1)   #5 * 4 *  3 * 2 * 1 * 1
#
# print(fact(3))  # Output: 120

#factorial(5) = 5 * 4 * 3 * 2 * 1


# def fibonacci(n):
#     if n == 1 or n==0:  # Base case
#         return n
#     else:  # Recursive case
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(10))  # Output: 8

# F(0)=0
#
# F(1)=1
#
# F(n)=F(n−1)+F(n−2) for n>1

# # BASE CASE
# F[0]=0
# F[1]=1
# # Recursive
# f(n) = f(n-1)+f(n-2)
# f(2) = f(1)+f(0) = 1
# f(3)  = f(2)+f(1) = 1+1 =2
# f(4)  = f(3) + f(2) = 2 + 1 =3

# def sum_of_digits(n):  #1234  #123  #12
#     if n == 0:  # Base case
#         return 0
#     else:  # Recursive case
#         return n % 10 + sum_of_digits(n // 10)
#
# print(sum_of_digits(2222))  # Output: 10




# def binary_search(arr, target, low, high):
#     if low > high:  # Base case: Target not found
#         return -1
#
#     mid = (low + high) // 2
#     if arr[mid] == target:  # Base case: Target found
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr, target, low, mid - 1)
#     else:
#         return binary_search(arr, target, mid + 1, high)
#
# # Usage
# arr = [1, 3, 5, 7, 9]
# print(binary_search(arr, 66, 0, len(arr) - 1))  # Output: 2


# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(50))  # Optimized with memoization

# Time & Space Complexity Recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

factorial(5)

































