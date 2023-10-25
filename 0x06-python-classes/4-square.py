#!/usr/bin/python3

'''
a class Square that defines a square by: (based on 3-square.py)

- Private instance attribute: size:
  o property def size(self): to retrieve it
  o property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception
        with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the
        message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area

@a_idk scripting
'''


class Square:
    '''class definition'''
    def __init__(self, size=0):  # initializing the class Square
        '''
        @size: private attribute (size of square)
        Raising the error using loops
        '''
#        if isinstance(size, int):
#            raise TypeError("size must be an integer")
#        elif size < 0:
#            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        '''getter'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''setter'''
        # raising exceptions
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''returning area of square'''
        return (self.__size * self.__size)
