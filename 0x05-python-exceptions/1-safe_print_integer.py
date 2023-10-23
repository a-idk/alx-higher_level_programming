#!/usr/bin/python3

'''
function that prints an integer with "{:d}".format()
@a_idk scripting
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Required print format
        # print()  # Newline print
        return True
    except TypeError:
        return False
    except ValueError:
        return (False)
