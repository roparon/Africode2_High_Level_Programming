#**************TASK2***************************
#Create a multiplication table in a clear and and organised manner. Use for loop.

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number*i)