print("The file running is", __name__)

def calculator(operator):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    if operator == "add":
        return add
    elif operator == "subtract":
        return subtract
    elif operator == "multiply":
        return multiply
    elif operator == "divide":
        return divide
    else:
        return "Invalid operator"

# result = calculator("add")(5, 3)
# print(f"The result is: {result}")

if __name__ == "__main__":
    result = calculator("add")(5, 3)
    print(f"The result is: {result}")