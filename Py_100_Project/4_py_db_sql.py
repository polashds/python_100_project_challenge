#Simple Calculator
def calculator():
    print("Simple Calculator")

    a = float(input("Enter first number:"))
    b = float(input("Enter the second number:"))
    operation = input("Choose an operation(+,-,*,/):")

    if operation == "+":
        result = a+b
    elif operation == "-":
        result = a-b
    elif operation == "*":
        result = a*b
    elif operation =="/":
        result = a/b

    else:
        result = "Invalid Operation"

    print("Result:", result)

calculator()


#Tags:
#Function, 
#user input, 
#Operation
#float

'''
This code defines a function calculator() 
that takes user input for two numbers and an operation (+, -, *, /), 
performs the specified operation, and prints the result. 
If the operation is not one of the four basic arithmetic operations, 
it prints "Invalid Operation".
'''