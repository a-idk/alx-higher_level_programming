#!/usr/bin/python3
import sys

'''
function that prints an integer
@a_idk scripting
'''


def safe_print_integer_err(value):
    check = True
    try:
        print("{:d}".format(value))
    except Exception as exception:
        print("Exception:", exception, file=sys.stderr)
        check = False
    return check
