"""
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("Welcome to Basic Python calculator")

while (True):
    numberOne = input('Enter first number : ')
    numberTwo = input('Enter second number : ')
    operator = input('Enter operator : ')
    if numberOne.isdigit() and numberOne.isdigit():
        inputOne = float(numberOne)
        inputTwo = float(numberOne)
        operatorList = ['+', '-', '*', '/']
        operation_dict = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        if operator in operatorList:
            operation = operation_dict.get(operator)
            try:
                print(inputOne, operator, inputTwo, "=", operation(inputOne, inputTwo))
            except ZeroDivisionError:
                print('Division cannot be done by zero.')
        else:
            print("Invalid Operator")
    else:
        print("Invalid numbers. Try again.")
    flag = input("Do you want to continue?\n Press any key to continue. \n Press X to exit.")
    if flag.lower() == 'x':
        break
