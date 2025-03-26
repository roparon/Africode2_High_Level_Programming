# def calculator():
#     operation = input("Enter the operation (+, -, *, /): ")
#     if operation not in ['+', '-', '*', '/']:
#         print("Error: Invalid operation!")
#         return

#     num1_input = input("Enter the first number: ")
#     num2_input = input("Enter the second number: ")

#     if not num1_input.replace('.', '', 1).isdigit() or not num2_input.replace('.', '', 1).isdigit():
#         print("Error: Invalid number!")
#         return

#     num1 = float(num1_input)
#     num2 = float(num2_input)

#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             print("Error: Cannot divide by zero!")
#             return
#         result = num1 / num2

#     print(f"The result of {num1} {operation} {num2} is: {result}")

# calculator()





# ASSIGNMENT:create a dynamic calculator using def where when you input a wrong operation it prints out an error statement, else it     provides answer in a descriptive manner

def calculator():
    num1_input = input("Enter the first number: ")
    if not num1_input.replace('.', '', 1).isdigit():
        print("Error: Invalid number!")
        return

    operation = input("Enter the operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        print("Error: Invalid operation!")
        return

    num2_input = input("Enter the second number: ")
    if not num2_input.replace('.', '', 1).isdigit():
        print("Error: Invalid number!")
        return

    num1 = float(num1_input)
    num2 = float(num2_input)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2

    print(f"The result of {num1} {operation} {num2} is: {result}")

calculator()

