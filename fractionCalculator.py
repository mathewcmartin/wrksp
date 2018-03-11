# Doing Math with Python Quizes

# Programming Challenges pg 22 - 26

# #4: Fraction Calculator

from fractions import Fraction

def add(a, b):
    print('Result of Addition: {0}'.format(a+b))

def subtract(a, b):
    print('Result of Subtraction: {0}'.format(a-b))

def division(a, b):
    print('Result of Division of the first fraction input by the second fraction input: {0}'.format(a/b))

def multiply(a, b):
    print('Result of Multiplication: {0}'.format(a*b))

if __name__ == '__main__':
    a = Fraction(input('Enter the first fraction: '))
    b = Fraction(input('Enter the second fraction: '))
    op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
    if op == 'Add':
        add(a,b)

    if op == 'Subtract':
        subtract(a,b)

    if op == 'Divide':
        division(a,b)

    if op == 'Multiply':
        multiply(a,b)
