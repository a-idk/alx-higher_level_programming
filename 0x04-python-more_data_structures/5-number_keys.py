#!/usr/bin/python3
def number_keys(a_dictionary):

    key_num = 0
    keys_lst = list(a_dictionary.keys())

    for x in keys_lst:
        key_num = key_num + 1
    return (key_num)
