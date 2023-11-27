#!/usr/bin/python3
"""
Title: Square.py
Description: class Square that inherits from Rectangle
@a_idk scripting
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square definition """

    def __init__(self, size=0, x=0, y=0, id=None):
        """
        Square class initialization/Contructor
        Args:
            size: size of square
            x: x point integer
            y: y point integer
            id: an integer
        """
        if size <= 0:
            raise ValueError("Size must be > 0")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Method that updates the rectangle given the args and keyword args
        Args:
            args: arguments
            kwargs: keyword arguments, i.e., key/value pairs
        """
        # since argument order is important, flag is used
        if args and len(args) != 0:
            flag = 0  # initializing the flag
            for index in args:
                if flag == 0:
                    if index is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = index
                elif flag == 1:
                    self.size = index
                elif flag == 2:
                    self.x = index
                elif flag == 3:
                    self.y = index
                flag = flag + 1
        # for keyword arguments `kwargs`, Argument order is not important
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.width = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
