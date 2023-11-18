#!/usr/bin/python3
"""
Title: Python Unittest suites for base.py
Description: creating the test suites for use with base.py
@a_idk scripting
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """
    Test case suite for Base class
    """
    def setUp(self):
        """ before every single test """
        Base._Base__nb_objects = 0
        pass

    def test_nb_objects_initialization(self):
        """ Testing for nb_objects initializing to zero """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_nb_objects_private(self):
        """ Testing for nb_objects is private attribute """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_base_instantiation(self):
        """ Testing for Base() instantiation """
        bs = Base()
        self.assertEqual(str(type(bs)), "<class 'models.base.Base'>")
        self.assertEqual(bs.__dict__, {"id": 1})

    def test_auto_increment_id(self):
        """ Testing automatic ID assignment in Base class """
        Base._Base__nb_objects = 0  # Ensure starting from a known state
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_base_instances_share_nb_objects(self):
        """Test that Base instances share the same __nb_objects attribute"""
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id, 1)
        self.assertEqual(bs2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_class_initialization(self):
        """ Testing for class initialization """
        with self.assertRaises(TypeError) as err:
            Base.__init__()
        message = (
                """Base.__init__() missing 1 required """
                """positional argument: 'self'"""
                )
        self.assertEqual(str(err.exception), message)

    def test_class_initialize_args(self):
        """ Testing initialization with arguments """
        with self.assertRaises(TypeError) as err:
            Base.__init__(self, 9, 3)
        message = (
                """Base.__init__() takes from 1 to 2 positional """
                """arguments but 3 were given"""
                )
        self.assertEqual(str(err.exception), message)

    def test_multiple_base_ids(self):
        """ Testing for consecutive base ids """
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id + 1, bs2.id)

    def test_instance_class_sync(self):
        """ Testing the sync in class & instance """
        bs = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), bs.id)

    def test_instance_class_sync2(self):
        """ Testing the sync between more class & instance """
        bs = Base()
        bs = Base(98)
        bs = Base("Hello")
        bs = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), bs.id)

    def test_custom_intID(self):
        """ Testing the custom integer identity """
        integer = 98
        bs = Base(integer)
        self.assertEqual(bs.id, integer)

    def test_custom_strID(self):
        """ Testing custom string identity """
        strng = "HelloWorld"
        bs = Base(strng)
        self.assertEqual(bs.id, strng)

    def test_kwargs_id(self):
        """ Testing kwargs id """
        x = 34
        bs = Base(id=x)
        self.assertEqual(bs.id, x)

    def test_to_json_string(self):
        """ Testing the to_json_string() method """
        # Testing missing argument
        with self.assertRaises(TypeError) as err:
            Base.to_json_string()
        msg = (
                """Base.to_json_string() missing 1 required """
                """positional argument: 'list_dictionaries'"""
                )
        self.assertEqual(str(err.exception), msg)
        # Testing with None and empty list
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        # Testing with data dictionaries
        data = [{'x': 123, 'y': 23423, 'width': 526271, 'id': 656352,
                'height': 34287}]
        self.assertEqual(len(Base.to_json_string(data)), len(str(data)))
        data = [{'x': 2, 'y': 4, 'width': 6, 'id': 8, 'height': 10}]
        self.assertEqual(len(Base.to_json_string(data)), len(str(data)))
        data = [{"low": 983421}]
        self.assertEqual(Base.to_json_string(data), '[{"low": 983421}]')
        data = [{"low": 983421}, {"dar": 224}, {"ME": 0}]
        self.assertEqual(
                Base.to_json_string(data),
                '''[{"low": 983421}, {"dar": 224}, {"ME": 0}]'''
                )
        data = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                {'x': 101, 'y': 20123, 'width': 312321, 'id': 656352,
                    'height': 34340}]
        self.assertEqual(len(Base.to_json_string(data)), len(str(data)))
        # Testing with empty dictionaries
        data = [{}]
        self.assertEqual(Base.to_json_string(data), '[{}]')
        data = [{}, {}]
        self.assertEqual(Base.to_json_string(data), '[{}, {}]')

        # Testing with Rectangle and Square objects
        rect1 = Rectangle(10, 7, 2, 8)
        dictionary = rect1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(2, 3, 4, 5)
        dictionary = [rect1.to_dictionary(), rect2.to_dictionary(),
                      rect3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rect1 = Square(10, 7, 2)
        dictionary = rect1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rect1 = Square(10, 7, 2)
        rect2 = Square(1, 2, 3)
        rect3 = Square(2, 3, 4)
        dictionary = [rect1.to_dictionary(), rect2.to_dictionary(),
                      rect3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_from_json_string(self):
        """ Testing the to_json_string() method """
        with self.assertRaises(TypeError) as err:
            Base.from_json_string()
        strng = (
                """Base.from_json_string() missing 1 required """
                """positional argument: 'json_string'"""
                )
        self.assertEqual(str(err.exception), strng)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        strng = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 656352, "height": 34340}]'
        data = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                {'x': 101, 'y': 20123, 'width': 312321, 'id': 656352,
                'height': 34340}]
        self.assertEqual(Base.from_json_string(strng), data)

        data = [{}, {}]
        strng = '[{}, {}]'
        self.assertEqual(Base.from_json_string(strng), data)
        data = [{}]
        strng = '[{}]'
        self.assertEqual(Base.from_json_string(strng), data)

        data = [{"low": 983421}, {"dar": 123}, {"ME": 0}]
        strng = '[{"low": 983421}, {"dar": 123}, {"ME": 0}]'
        self.assertEqual(Base.from_json_string(strng), data)

        data = [{"low": 983421}]
        strng = '[{"low": 983421}]'
        self.assertEqual(Base.from_json_string(strng), data)

        data = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        strng = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(strng), data)

        data = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 656352,
                'height': 34340}]
        strng = '[{"x": 101, "y": 20123, "width": 312321, "id": 656352, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(strng), data)

        in_lst = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        out_lst = Rectangle.from_json_string(
            Rectangle.to_json_string(in_lst))
        self.assertEqual(in_lst, out_lst)

    def test_load_from_file_rectangle(self):
        """ Testing the load_from_file() method for Rectangle objects """
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        in_lst = [rect1, rect2]
        Rectangle.save_to_file(in_lst)
        out_lst = Rectangle.load_from_file()
        self.assertNotEqual(id(in_lst[0]), id(out_lst[0]))
        self.assertEqual(str(in_lst[0]), str(out_lst[0]))
        self.assertNotEqual(id(in_lst[1]), id(out_lst[1]))
        self.assertEqual(str(in_lst[1]), str(out_lst[1]))

    def test_load_from_file_square(self):
        """ Testing the load_from_file() method for Square objects """
        sqr1 = Square(5)
        sqr2 = Square(7, 9, 1)
        in_lst = [sqr1, sqr2]
        Square.save_to_file(in_lst)
        out_lst = Square.load_from_file()
        self.assertNotEqual(id(in_lst[0]), id(out_lst[0]))
        self.assertEqual(str(in_lst[0]), str(out_lst[0]))
        self.assertNotEqual(id(in_lst[1]), id(out_lst[1]))
        self.assertEqual(str(in_lst[1]), str(out_lst[1]))

    def test_save_to_file(self):
        """Testing the save_to_file() method """
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        Rectangle.save_to_file([rect1, rect2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        # considering the Rectangle object
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rect2 = Rectangle(2, 4)
        Rectangle.save_to_file([rect2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        # considering the Square object
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rect2 = Square(1)
        Square.save_to_file([rect2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    def test_create(self):
        """ Testing the create() method """
        rect1 = Rectangle(3, 5, 1)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual(str(rect1), str(rect2))
        self.assertFalse(rect1 is rect2)
        self.assertFalse(rect1 == rect2)

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_two_rectangles(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", file.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file_csv_one_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8", file.read())

    def test_save_to_file_csv_two_squares(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2\n3,8,1,2", file.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual("", file.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual("", file.read())

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_second_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_first_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sqr1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sqr2), str(list_squares_output[1]))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

    def test_load_from_file_csv_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))


if __name__ == "__main__":
    unittest.main()
