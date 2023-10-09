#!/usr/bin/python3
# @a_idk scripting

# function that finds all multiples of 2 in a list.


def divisible_by_2(my_list=[]):
    # initializing the list
    x_times = []

    for num in range(len(my_list)):
        if my_list[num] % 2 != 0:
            x_times.append(False)
        else:
            x_times.append(True)
    return (x_times)
