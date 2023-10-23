#!/usr/bin/python3

'''
function that prints an integer with "{:d}".format()
@a_idk scripting
'''


def safe_print_integer(value):
    try:
        get_input = int(value)  # integer value input
        print("{:d}".format(get_input))  # Required print format
        # print()  # Newline print
        return (True)
    except (TypeError):
        return (False)
    except (ValueError):
        return (False)
