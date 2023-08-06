# Creating fucntions for the calculator

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

num1 = int(input("Type numebr one: "))
num2 = int(input("Typer number two: "))

operation = input("Choose operation: ")

if operation == "sum":
    print(sum(num1, num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "mult":
    print(mult(num1, num2))
elif operation == "div":
    print(div(num1, num2))