#!/usr/bin/python3
import math

'''
Python class MagicClass that does exactly the same as the following
Python bytecode
@a_idk scripting
'''

# define class MagicClass
class MagicClass:
    ''' MagicClass definition '''
    def __init__(self, radius=0):
        ''' Initializing the class '''
        self.__radius = 0
        ''' handling exception '''
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        ''' Calculates Area of Circle '''
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        ''' calculates circumference of circle '''
        return (math.pi * self.__radius * 2)
