#!/usr/bin/python3

'''
a class Square that defines a square by: (based on 0-square.py)
- Private instance attribute: size
- Instantiation with size (no type/value verification)
- You are not allowed to import any module
@a_idk scripting
'''


class Square:
    '''class definition'''
    def __init__(self, size):  # initializing the class Square
        # @size: private attribute (size of square)
        self.__size = size
