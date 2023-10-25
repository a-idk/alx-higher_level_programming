#!/usr/bin/python3

'''
a class Square that defines a square by: (based on 4-square.py)

@a_idk scripting
'''


class Square:
    """Class definition"""
    def __init__(self, size=0, position=(0, 0)):  # initializing
        '''
        @size: private attribute (size of square)
        Raising the error using loops
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter"""
        # raising exceptions
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returning area of square"""
        return (self.__size**2)

    def my_print(self):
        """handling prints"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            # print new line
            print("")









