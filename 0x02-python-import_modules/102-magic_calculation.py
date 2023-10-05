#!/usr/bin/python3
# @a_idk scripting


def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a >= b:
        return (sub(a, b))
    else:
        # setting the addition to result
        result = add(a, b)
        for x in range(4, 6):
            result = add(result, x)
        return (result)
