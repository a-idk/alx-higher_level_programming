#!/usr/bin/python3
# import sys

'''
function that does exactly the same as the following Python bytecode
@a_idk scripting
'''


def magic_calculation(a, b):
    # initializing the outcome/result
    outcome = 0
    for x in range(1, 3):
        try:
            if a < x:
                raise Exception('Too far')
            outcome = outcome + (a ** b) / x
        except Exception:
            outcome = a + b
            break
        return outcome
