#!/usr/bin/python3
"""
Title: 2-rectangle.py
Description: Write a class Rectangle that defines a rectangle by:
            (based on 1-rectangle.py)
Author: @a_idk Scripting
"""


class Rectangle:
    """
    Class Name: Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializing the class instance 'Rectangle'
        Args:
            height: instance for height of Rectangle
            width: instance for width of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value: positive integer width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value: positive integer height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """
        return perimeter of rectangle
        """
        if self.__width == 0:
            return (0)
        elif self.__height == 0:
            return (0)
        return ((self.__width * 2) + (2 * self.__height))

    def area(self):
        """
        Return the area of the rectangle
        """
        return (self.__height * self.__width)
