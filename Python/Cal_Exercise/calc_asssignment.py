print("Hello, welcome to Rop's calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
print("The sum is:", sum)

difference = num1 - num2
print("The difference is:", difference)

product = num1 * num2
print("The product is:", product)

if num2 != 0:
    division = num1 / num2
    print("The division is:", division)
else:
    print("Sorry, you can't divide by zero!")
