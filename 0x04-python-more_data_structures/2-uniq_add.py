#!/usr/bin/python3
# @a_idk scripting

# function that adds all unique integers in a list
# (only once for each integer)


def uniq_add(my_list=[]):
    # initializing and setting the variable
    summed = 0
    lst = set(my_list)

    # populating the 
    for idx in lst:
        summed = summed + idx
    return (summed)
