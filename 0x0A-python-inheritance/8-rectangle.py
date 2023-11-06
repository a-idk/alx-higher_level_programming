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
