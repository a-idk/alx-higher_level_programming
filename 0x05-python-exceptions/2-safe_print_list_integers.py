#!/usr/bin/python3

'''
function that prints the first x elements of a list and only integers
@a_idk scripting
'''


def safe_print_list_integers(my_list=[], x=0):
    # initializing variables
    indx1 = 0
    indx2 = 0
    while x > indx1:
        try:
            print("{:d}".format(my_list=[indx1]), end="")
            indx2 = indx2 + 1
        except (TypeError, ValueError):
            pass
        indx1 = indx1 + 1
    print()  # Newline character
    return (indx2)
