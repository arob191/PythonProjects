#Calculator

import os

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary of Functions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    num1 = float(input('What is the first number? \n'))

    for symbol in operations:
        print(symbol)

    # While Loop to continue calculations:

    Continue = True

    while Continue:
        
        operation_symbol = input("Pick an operation \n")
        new_num = float(input('What is the next number? \n'))
        calculation_function = operations[operation_symbol]
        
        answer = calculation_function(num1, new_num)
        
        print(f"{num1} {operation_symbol} {new_num} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.:") == "y":
            num1 = answer
        else:
            Continue = False
            os.system('cls')
            calculator()
        
        os.system('cls')

calculator()