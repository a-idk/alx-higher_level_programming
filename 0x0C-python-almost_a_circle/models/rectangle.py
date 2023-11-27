#!/usr/bin/python3
"""
Title: Rectangle.py
Description: class Rectangle that inherits from Base
@a_idk scripting
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle definition """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle class initialization/Contructor
        Args:
            width: rectangle's width
            height: rectangle's height
            x: x point integer
            y: y point integer
            id: an integer
        Raises:
            TypeError: If width||height||x||y is not integer
            ValueError: If width||height <= 0 or x||y < 0
        """
        if width is None or height is None:
            raise TypeError(
                    """__init__() missing 1 or more required positional """
                    """argument"""
                    )
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be > 0")
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("X and Y must be integers")
        if x < 0 or y < 0:
            raise ValueError("X and Y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value: positive integer width value
        """
        if not isinstance(value, int):
            # if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value: positive integer height value
        """
        if not isinstance(value, int):
            # if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x point getter """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        Args:
            value: zero or positive integer x value
        """
        # if type(value) != int:
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """
        x setter
        Args:
            value: zero or positive integer x value
        """
        # if type(value) != int:
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.width * self.height

    def to_dictionary(self):
        """
        Method that returns dictionary
        """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}

    def __str__(self):
        """
        Method that returns print() and str() representation
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                self.id, self.x, self.y, self.width, self.height))

    def display(self):
        """
        Represents the cectangle using the # symbol
        """
        # check for zero value in height or weight
        if self.width == 0 or self.height == 0:
            print("")
            return
        for y in range(self.y):
            print("")
        for hgt in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for wid in range(self.width):
                print("#", end="")
            print("")

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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = index
                elif flag == 1:
                    self.width = index
                elif flag == 2:
                    self.height = index
                elif flag == 3:
                    self.x = index
                elif flag == 4:
                    self.y = index
                flag = flag + 1
            """ for keyword args `kwargs`, Arg order is not important """
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    if val is not None and val < 0:
                        raise ValueError("x must be >= 0")
                    self.x = val
                elif key == "y":
                    if val is not None and val < 0:
                        raise ValueError("y must be >= 0")
                    self.y = val
