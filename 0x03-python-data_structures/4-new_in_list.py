#!/usr/bin/python3
# @a_idk scripting

# function that replaces an element in a list at a specific position
# without modifying the original list (like in C).


def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    elif idx > (len(my_list) - 1):
        return (my_list)
    else:
        cp = [i for i in my_list]
        cp[idx] = element
        return (cp)
