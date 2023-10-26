#!/usr/bin/python3
import math

'''
Python class MagicClass that does exactly the same as the following
Python bytecode
@a_idk scripting
'''


# define class MagicClass
class MagicClass:
    '''
    MagicClass definition
    Attributes:
        radius: radius
    '''
    def __init__(self, radius=0):
        '''
        Initializing the class
        Args:
            radius: radius.
        Raises:
            TypeError: radius must be a number
        '''
        self.__radius = 0
        ''' handling exception '''
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def circumference(self):
        '''
        Calculates circumference of circle
        Returns: circumference
        '''
        return (math.pi * self.__radius * 2)

    def area(self):
        '''
        Calculates Area of Circle
        Returns: area
        '''
        return (math.pi * self.__radius ** 2)
