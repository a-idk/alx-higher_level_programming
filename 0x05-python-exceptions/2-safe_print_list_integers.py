#!/usr/bin/python3

'''
function that prints the first x elements of a list and only integers
@a_idk scripting
'''


def safe_print_list_integers(my_list=[], x=0):
    # initializing variables
    indx1 = 0

    try:
        for i in range(x):
            try:
                print("{:d}".format(int(my_list[i])), end="")
                indx1 = indx1 + 1
            except ValueError:
                pass
            except TypeError:
                pass
            except IndexError:
                if i == 0:
                    print()
                    break
                else:
                    raise
        print()  # Newline character
    except TypeError:
        print("Error: List input not found! Try again!")
    return (indx1)
