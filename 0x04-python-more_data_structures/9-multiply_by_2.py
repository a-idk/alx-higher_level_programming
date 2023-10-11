#!/usr/bin/python3
# @a_idk scripting

#  function that returns a new dictionary with
# all values multiplied by 2


def multiply_by_2(a_dictionary):
    # setting the list
    dictionary = a_dictionary.copy()
    keys_lst = list(dictionary.keys())
    # populating dictionary with new values
    for element in keys_lst:
        dictionary[element] = dictionary[element] * 2
    return (dictionary)
