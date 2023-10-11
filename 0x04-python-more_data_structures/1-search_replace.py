#!/usr/bin/python3
# @a_idk scripting

# function that replaces all occurrences of an element
# by another in a new list


def search_replace(my_list, search, replace):
    # populating the initial list
    new_list = list(map(lambda e: replace if e == search else e, my_list))
    return (new_list)
