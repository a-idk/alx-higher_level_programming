#!/usr/bin/python3
# @a_idk scripting

# function that returns the number of keys in a dictionary.


def number_keys(a_dictionary):
    # initializing the numbering
    keys_lst = list(a_dictionary.keys())
    key_num = 0

    # counting the keys
    for x in keys_lst:
        key_num = key_num + 1
    return (key_num)
