#!/usr/bin/python3

'''
function that prints x elements of a list
@a_idk scripting
'''


def safe_print_list(my_list=[], x=0):
    try:
        element = 0  # initializing the count for num of element
        for i in my_list:
            if x > element:
                print(i, end="")
                element = element + 1
        print()
        return (element)
    except TypeError:
        print("Error: Input is not a list! Try again!")
        return (0)
