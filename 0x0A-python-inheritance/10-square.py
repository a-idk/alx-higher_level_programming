#!/usr/bin/python3
"""
Title: Square module
Description: Write a class Square that inherits from Rectangle
        (9-rectangle.py)
@a_idk Scripting
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a classs Square with Rectangle inheritance """
    def __init__(self, size):
        """
        - COntructor
        initializing the class with args width and height
        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computing the area of Square
        """
        return self.__size * self.__size
