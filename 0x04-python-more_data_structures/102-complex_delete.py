#!/usr/bin/python3
# @a_idk scripting

# function that deletes keys with a specific value in a dictionary


def complex_delete(a_dictionary, value):
    # setting the key list
    keys_lst = list(a_dictionary.keys())
    # populating the dictionary
    for idx in keys_lst:
        if value == a_dictionary.get(idx):
            del a_dictionary[idx]
    return (a_dictionary)
