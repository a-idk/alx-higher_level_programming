#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    summer = add(a, b)
    subtracter = sub(a, b)
    multiplier = mul(a, b)
    divider = div(a, b)

    print(f"{a} + {b} = {summer}")
    print(f"{a} - {b} = {subtracter}")
    print(f"{a} * {b} = {multiplier}")
    print(f"{a} / {b} = {divider}")
