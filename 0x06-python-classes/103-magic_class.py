#!/usr/bin/python3
import math

'''
Python class MagicClass that does exactly the same as the following
Python bytecode
@a_idk scripting
'''


class MagicClass:
    """ MagicClass definition """
    def __init__(self, rad=0):
        """ Initializing the class """
        self.__rad = 0
        ''' handling exception '''
        if not isinstance(rad, int) and not isinstance(rad, float):
            raise TypeError("radius must be a number")
        else:
            self.__rad = rad

    def circumference(self):
        """ calculates circumference of circle """
        return (math.pi * self.__rad * 2)
    
    def area(self):
        """ Calculates Area of Circle """
        return (math.pi * self.__rad ** 2)
