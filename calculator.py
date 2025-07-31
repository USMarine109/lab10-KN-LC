"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/USMarine109/lab10-swe
# Partner 1: Kenneth Nguyen
# Partner 2: Lauren Castello

import math
# First example
def add(a, b): 
    return a + b    

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def exp(a, b):
    return math.exp(a, b)

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)


