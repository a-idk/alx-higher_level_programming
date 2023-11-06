#!/usr/bin/python3
"""
Title: Integer validator/Improved Geometry module
Description: Write a class BaseGeometry (based on 6-base_geometry.py)
@a_idk Scripting
"""


class BaseGeometry:
    """ defines a classs BaseGeometry """
    def area(self):
        """
        Method/Function that raises an Exception with the message
        area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validating the value
        Args:
            name: name of parameter givern
            value: parameter to be validated
        Raise:
            TypeError when value is not inteeger
            ValueError when value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
