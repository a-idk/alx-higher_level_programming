#!/usr/bin/python3
# @a_idk scripting

# function that prints a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):
    # initializing the list
    ordered_lst = list(a_dictionary.keys())
    # sorting the list
    ordered_lst.sort()
    # printing out the sorted list
    for idx in ordered_lst:
        print("{}: {}".format(idx, a_dictionary.get(idx)))
