#This is a nested function example
def calculator(operation):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):     
        return a/b
    if operation == 'add':
        return add
    elif operation == 'sub':
        return sub
    if operation == 'mul':
        return mul
    if operation == 'div':
        return div
    else:
        return "Invalid operand"
results_add = calculator("add")(2,3)
print(f"Addition results:{results_add}")