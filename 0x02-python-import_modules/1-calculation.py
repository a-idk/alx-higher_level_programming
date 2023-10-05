#!/usr/bin/python3

# @a_idk scripting

'''program that imports functions from the file calculator_1.py,
does some Maths, and prints the result.'''

if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul

    # defining and initializing variables
    a = 10
    b = 5

    # mathematical computations
    summer = add(a, b)
    subtracter = sub(a, b)
    multiplier = mul(a, b)
    divider = div(a, b)

    # output displays
    print(f"{a} + {b} = {summer}")
    print(f"{a} - {b} = {subtracter}")
    print(f"{a} * {b} = {multiplier}")
    print(f"{a} / {b} = {divider}")
