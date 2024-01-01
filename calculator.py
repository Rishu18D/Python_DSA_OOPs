


##############################################################################
#program to create calculator

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations = {1: sum, 2: sub, 3: multiply, 4: divide}

operation=int(input("Enter the operation 1/2/3/4:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if operation in operations:
    print("Result:", operations.operation)
else:
    print("You entered an invalid operator!!!!")
