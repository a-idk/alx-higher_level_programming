#!/usr/bin/python3
"""
Title: Rectangle module
Description: Write a class Rectangle that inherits from BaseGeometry
        (7-base_geometry.py).
@a_idk Scripting
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a classs Rectangle with BaseGeometry inheritance """
    def __init__(self, width, height):
        """
        - COntructor -
        initializing the class with args width and height
        Args:
            width: width of rectangle
            heigth: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Computing the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        The string representation
        """
        str_rep = "[" + str(self.__class__.__name__) + "] "
        str_rep += str(self.__width) + "/" + str(self.__height)
        return str_rep
