# Recursive function to find the sum of 
# numbers from 0 to n
# def find_sum(n):
    # Base case 
    # if n == 1:
    #     return 1
    
    # Recursive case 
#     return n + find_sum(n - 1)

# n = 5
# print(find_sum(n))


# Factorial function using recursion
# def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case
#     return n * factorial(n - 1)

# n = 5
# print(factorial(n))


# Fibonacci sequence using recursion
# def fibonacci(n):
#     # Base case
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = 5
# print(fibonacci(n))




# # Exercise 1: Factorial using recursion
# def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case
#     return n * factorial(n - 1)

# n = 10
# print(factorial(n))



def fact(n):
    # BASE CONDITION
    if n == 0:
        return 1
    return n * fact(n - 1)

print("Factorial of 5 : ", fact(5))
