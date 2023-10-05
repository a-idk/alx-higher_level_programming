#!/usr/bin/python3

# @a_idk scripting

'''program that imports functions from the file calculator_1.py,
does some Maths, and prints the result.'''

if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul

    # defining and initializing variables
    a = 10
    b = 5

    # mathematical calculations
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
