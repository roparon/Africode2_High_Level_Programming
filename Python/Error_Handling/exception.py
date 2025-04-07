# from math import kirui
# print{"print_function"}
# a = 1
# b = 2

# def divide(a, b):
#     return a / b

# result = divide(1, 0)
# print(result)

# try:
#     result = 1 / 0
#     print(result)
# except ZeroDivisionError as e:
#     print(f"Error {e}")
# except TypeError:
#     print("Invalid input")
# except:
#     print("An error occured")
# else:
#     print("Execution was successful!")
# finally:
#     ("I am being executed")




#*******************SYNTAX/COMPILE ***-- Happen when you've written code that Python doesn't understands
#*******************intendation Error*****************************
# def func():
#     return None


#******************Syntax Error ***********************************
# def func():
#     return None

#******************Exception/Runtime Error*-----Happens during excecution of a programm
# print("Hello" + 5)


#**************************Name Error*******************************
# print(Dorothy)
#       other exception error
"""
- ValueError
-ZeroDivisionError
-KeyError
-IndexError
-FileNotFoundError
"""

#***********Logical Errors*********
# def sum(a,b):
#     return a/b
# result = sum (10, 3)
# print(result)

try:
    number = int(input("Enter a number: "))
    results = 10/number
except Exception as e:
    print(f"Error: {e}")
else:
    print(results)
finally:
    print("Thanks for using our Calc programm")