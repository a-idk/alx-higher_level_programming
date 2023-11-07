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

    def print_sorted(self):
        """
        Method that prints the list, but sorted
        (Ascending order)
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
