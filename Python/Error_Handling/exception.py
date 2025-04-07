# from math import kirui
# print{"print_function"}
a = 1
b = 2

def divide(a, b):
    return a / b

# result = divide(1, 0)
# print(result)

try:
    result = 1 / 0
    print(result)
except ZeroDivisionError as e:
    print(f"Error {e}")
except TypeError:
    print("Invalid input")
except:
    print("An error occured")
else:
    print("Execution was successful!")
finally:
    ("I am being executed")