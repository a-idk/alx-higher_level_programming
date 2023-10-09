#!/usr/bin/python3
# @a_idk scripting

# function that prints all integers of a list, in reverse order.


def print_reversed_list_integer(my_list=[]):
#    my_list.reverse()
#    for idx in range(len(my_list) - 1, -1, -1):
#        print("{:d}".format(my_list[idx]))
#    for idx in my_list:
#        print("{:d}".format(idx))
     if isinstance(my_list, list):
        my_list.reverse()
        for idx in my_list:
            print("{:d}".format(idx))
