#!/usr/bin/python3
# @a_idk scripting

# function that returns the weighted average
# of all integers tuple (<score>, <weight>)


def weight_average(my_list=[]):
    # if list is empty
    if not my_list:
        return 0
    # initialing variables
    up, down = 0, 0

    for idx in my_list:
        # weighted average
        up = up + idx[0] * idx[1]
        down = down + idx[1]
    return (up / down)
