"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b
    pass

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a raise ZeroDivisionError if a == 0

def log(a, b):
    return log(b, a) raise ValueError

def exp(a, b):
    return exp(a, b)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

