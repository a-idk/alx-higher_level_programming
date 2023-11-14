#!/usr/bin/python3
"""
Title: Base.py
Descriptiion: Write the first class Base. This class will be the “base”
        of all other classes in this project
@a_idk scripting
"""
import json
import csv
from os import path
from models.rectangle import Rectangle
from models.square import Square
import turtle as tu
import time
from random import randrange


class Base:
    """ Class Base definition with private class attribute __nb_objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class Initialization/Constructor
        Args:
            id: an integer
        """
        # assigning the public instance attribute
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converting a list of dictionaries into a JSON string
        Args:
            list_dictionaries: List of dictionaries
        """

        if list_dictionaries is None:
            return ("[]")
        if not list_dictionaries:
            return ("[]")
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes an object to a text file
        using JSON representation
        Args:
            cls: class object
            list_objs: filename of the file to be written to
        """
        fd = cls.__name__ + ".json"
        with open(fd, "w") as jsf:
            # with autocloses after suite finishes
            if list_objs is None:
                jsf.write("[]")
            else:
                tmp = []
                for item in list_objs:
                    tmp.append(item.to_dictionary())
                list_objs = tmp
                jsf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converting a JSON string to a list dictionary
        Args:
            json_string: JSON string
        """
        if json_string is None:
            return []
        if not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method that creates/loads instance from given dictionary
        Args:
            cls: class object or filename
            dictionary: the dictionary
        """
        if cls is Square:
            new_shape = Square(1)
        elif cls is Rectangle:
            new_shape = Rectangle(1, 1)
        else:
            new_shape = None
        new_shape.update(**dictionary)
        return new_shape

    @classmethod
    def load_from_file(cls):
        """
        Method that Loads JSON string from file and converts to string
        Args:
            cls: class object or filename
        """
        fd = "{}.json".format(cls.__name__)
        # checking if file exist
        if not path.isfile(fd):
            return []
        with open(fd, "r", encoding="utf-8") as file:
            file_json = cls.from_json_string(file.read())
            new_obj = [cls.create(**idx) for idx in file_json]
            return new_obj

    @classmethod
    def load_from_file_csv(cls):
        """
        Method that loads object to csv file
        """
        filename = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            csv_read = csv.reader(file)
            for rw in csv_read:
                rw = [int(r) for r in rw]
                if cls is not Rectangle:
                    data = {"id": rw[0], "size": rw[1],
                            "x": rw[2], "y": rw[3]}
                else:
                    data = {"id": rw[0], "width": rw[1], "height": rw[2],
                            "x": rw[3], "y": rw[4]}
                filename.append(cls.create(**data))
        return filename

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Method that saves object to file (CSV)
        Args:
            cls: class object
            list_objs: filename of the file to be written to
        """
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as file:
            # writer = csv.writer(f), writer.writerows(list_objs)
            csv.writer(file).writerows(list_objs)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Method that opens a window and draws all the Rectangles and Squares
        """
        tu.Screen().colormode(255)
        for idx in list_rectangles + list_squares:
            t = tu.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((idx.x + t.pos()[0], idx.y - t.pos()[1]))
            t.pensize(10)
            t.forward(idx.width)
            t.left(90)
            t.forward(idx.height)
            t.left(90)
            t.forward(idx.width)
            t.left(90)
            t.forward(idx.height)
            t.left(90)
            t.end_fill()
        time.sleep(5)
