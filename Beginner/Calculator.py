#Calculator


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

num1 = int(input('What is the first number? \n'))
num2 = int(input('What is the second number? \n'))


for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: \n")

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")