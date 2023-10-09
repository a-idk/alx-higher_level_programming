#!/usr/bin/python3
# @a_idk scripting

#function that removes all characters c and C from a string.


def no_c(my_string):
    new_str = [x for x in my_string if x != 'C' and x != 'c']
    return ("".join(new_str))
