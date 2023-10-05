#!/usr/bin/python3
# @a_idk scripting


if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    # defining and initializing variables
    a = 10
    b = 5

    # mathematical computations
    out_plus = add(a, b)
    out_minus = sub(a, b)
    out_mult = mul(a, b)
    out_div = div(a, b)

    # outputting
    print("{} + {} = {}".format(a, b, out_plus))
    print("{} - {} = {}".format(a, b, out_minus))
    print("{} * {} = {}".format(a, b, out_mult))
    print("{} / {} = {}".format(a, b, out_div))
