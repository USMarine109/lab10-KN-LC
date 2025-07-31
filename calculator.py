#https://github.com/USMarine109/lab10-swe
# Partner 1: Kenneth Nguyen
# Partner 2: Lauren Castello

'''
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
'''

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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def exp(a, b):
    return math.exp(a, b)

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)


