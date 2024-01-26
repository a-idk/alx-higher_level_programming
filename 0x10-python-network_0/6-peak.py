#!/usr/bin/python3
# Title: Find a peak
# Description: Write a fxn that finds a peak in list of unsorted integers


def find_peak(list_of_integers):
    """
    find a peak Module
    """
    if (not list_of_integers) or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        result = list_of_integers[0]
        return result
    if len(list_of_integers) == 2:
        result = max(list_of_integers)
        return result

    num = len(list_of_integers)
    centre = int(num / 2)
    high_num = list_of_integers[centre]
    pos = centre + 1
    neg = centre - 1

    if high_num > list_of_integers[neg] and high_num > list_of_integers[pos]:
        return high_num
    elif high_num < list_of_integers[neg]:
        return find_peak(list_of_integers[:centre])
    else:
        return find_peak(list_of_integers[pos:])
