#!/usr/bin/python3
# @a_idk scripting

# function that retrieves an element from a list like in C.


def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > (len(my_list) - 1):
        return (None)
    else:
        return (my_list[idx])
