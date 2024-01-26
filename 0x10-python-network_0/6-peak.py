#!/usr/bin/python3
# Title: Find a peak
# Description: Write a fxn that finds a peak in list of unsorted integers


def find_peak(list_of_integers):
    """
    find a peak Module
    """
    if ((len(list_of_integers) == 0) or (not list_of_integers)):
        return None

    if list_of_integers:
        list_of_integers.sort(reverse=True)
        result = list_of_integers[0]
        return result
