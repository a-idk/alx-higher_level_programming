#!/usr/bin/python3
"""
Title: My list
Description: A class MyList that inherits from list
@a_idk Scripting
"""


class MyList(list):
    """
    Class myList definition
    """
    pass
    def print_sorted(self):
        """
        Method that prints the list, but sorted
        (Ascending order)
        """
        print(sorted(list(self)))
