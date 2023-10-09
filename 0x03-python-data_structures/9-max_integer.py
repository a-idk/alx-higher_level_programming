#!/usr/bin/python3
# @a_idk scripting

# function that finds the biggest integer of a list.


def max_integer(my_list=[]):
    # Check if list is empty
    if len(my_list) == 0:
        return (None)
    # Assuming list contains only integer
    # Assigning the first element
    biggest_num = my_list[0]
    for num in range(len(my_list)):
        # Comparing the numbers
        if my_list[num] > biggest_num:
            biggest_num = my_list[num]
    return (biggest_num)
