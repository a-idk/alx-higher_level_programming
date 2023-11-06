#!/usr/bin/python3
"""
Title: My integer
Description: Write a class MyInt that inherits from int
@a_idk Scripting
"""


class MyInt(int):
    """
    class definition for MyInt with inheritances from int
    """
    def __init__(self, my_int):
        """
        - Contructor -
        initializing the class MyInt
        Args:
            my_int: int to be used for overriding
        """
        self.my_int = my_int

    @property
    def my_int(self):
        """
        my_int getter
        """
        return self.__my_int

    @my_int.setter
    def my_int(self, my_int):
        """
        setter method
        """
        if type(my_int) is not int:
            raise TypeError("my_int must be an integer")
        self.__my_int = my_int

    def __eq__(self, value):
        """
        equal method to
        """
        if self.my_int == value:
            return False
        return True

    def __ne__(self, value):
        """
        not equal to method
        """
        if self.my_int != value:
            return False
        return True
