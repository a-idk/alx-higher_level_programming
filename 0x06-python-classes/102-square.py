#!/usr/bin/python3

'''
a class Square that defines a square by: (based on 4-square.py)

@a_idk scripting
'''


class Square:
    '''class definition'''
    def __init__(self, size=0):
        ''' Initializing the class '''
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

    def __eq__(self, comp):
        ''' compare if equal (==) '''
        return self.__size == comp.__size

    def __ne__(self, comp):
        ''' compare not equal to (!=)'''
        return self.__size != comp.__size

    def __gt__(self, comp):
        ''' compare greater than (>) '''
        return self.__size > comp.__size

    def __ge__(self, comp):
        ''' compare greater than or equal to (>=) '''
        return self.__size >= comp.__size

    def __lt__(self, comp):
        ''' compare less than (<) '''
        return self.__size < comp.__size

    def __le__(self, comp):
        ''' compare greater than or equal to (<=) '''
        return self.__size <= comp.__size
