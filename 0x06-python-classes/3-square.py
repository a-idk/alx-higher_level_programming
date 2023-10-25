#!/usr/bin/python3

'''
a class Square that defines a square by: (based on 2-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
  o "size must be an integer", otherwise raise a TypeError exception with the
    message size must be an integer
  o if size is less than 0, raise a ValueError exception with the message
    "size must be >= 0"
- Public instance method: def area(self): that returns the current square area
- importing module is not allowed

@a_idk scripting
'''


class Square:

    def __init__(self, size=0):  # initializing the class Square
        '''
        @size: private attribute (size of square)
        Raising the error using loops
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        # returning area of square
        return (self.__size * self.__size)
