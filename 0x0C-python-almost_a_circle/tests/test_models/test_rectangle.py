#!/usr/bin/python3
"""
Title: Python Unittest suites for rectangle.py
Description: creating the test suites for use with rectangle.py
@a_idk scripting
"""
import unittest
from contextlib import redirect_stdout
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from random import randrange


class TestRectangle(unittest.TestCase):
    """
    Test case suite for Rectangle class
    """
    def setUp(self):
        """ before every single test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ after every single test """
        pass

    def test_initialization(self):
        """ Testing the class initialization """
        with self.assertRaises(TypeError) as err:
            rect = Rectangle()
        stg = (
                """__init__() missing 2 required positional """
                """arguments: 'width' and 'height'"""
                )
        self.assertEqual(str(err.exception), stg)

    def test_args_initialization(self):
        """Testing the class Rectangle initialization with args """
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(2, 2, 8, 9, 5, 7)
        stg = (
                """__init__() takes from 3 to 6 positional """
                """arguments but 7 were given"""
                )
        self.assertEqual(str(err.exception), stg)

    def test_arg_initialization(self):
        """ Testing the class Rectangle initialization with 1 arg """
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1)
        stg = (
                """__init__() missing 1 required positional """
                """argument: 'height'"""
                )
        self.assertEqual(str(err.exception), stg)

    def test_class_rect(self):
        """ Testing the Rectangle class """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_inheritance(self):
        """ Testing the Rectangle class Base inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instantiation(self):
        """ Testing the class instantiation """
        rect = Rectangle(15, 30)
        self.assertEqual(str(type(rect)),
                         "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rect, Base))
        data = {'_Rectangle__height': 30, '_Rectangle__width': 15,
                '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rect.__dict__, data)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle("me", 2)
        message = "width must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, "me")
        message = "height must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, 2, "me")
        message = "x must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, 2, 3, "me")
        message = "y must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(-3, 2)
        message = "width must be > 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(2, -3)
        message = "height must be > 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(0, 4)
        message = "width must be > 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(4, 0)
        message = "height must be > 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(1, 3, -6)
        message = "x must be >= 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(1, 2, 4, -6)
        message = "y must be >= 0"
        self.assertEqual(str(err.exception), message)

    def test_position_instantiation(self):
        """ Testing the positional instantiation """
        rect = Rectangle(5, 10, 15, 20)
        data = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(rect.__dict__, data)

        rect = Rectangle(5, 10, 15, 20, 98)
        data = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(rect.__dict__, data)

    def test_kwargs_instantiation(self):
        """Testing kwargs instantiation """
        rect = Rectangle(100, 200, id=421, y=99, x=101)
        data = {'_Rectangle__height': 200, '_Rectangle__width': 100,
                '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rect.__dict__, data)

    def test_id_inheritance(self):
        """Testing for id inheritance from Base """
        Base._Base__nb_objects = 98
        rect = Rectangle(2, 4)
        self.assertEqual(rect.id, 99)

    def test_properties(self):
        """ Testing for getter getters/setters """
        rect = Rectangle(5, 9)
        rect.width = 100
        rect.height = 101
        rect.x = 102
        rect.y = 103
        data = {'_Rectangle__height': 101, '_Rectangle__width': 100,
                '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(rect.__dict__, data)
        self.assertEqual(rect.width, 100)
        self.assertEqual(rect.height, 101)
        self.assertEqual(rect.x, 102)
        self.assertEqual(rect.y, 103)

    def invalid_types(self):
        """ Returns tuple of types for validation """
        typ = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
               [4], {5}, {6: 7}, None)
        p = (1.5, -1, float('inf'), float('-inf'), True, "str", (2,), [4],
                None)
        return p

    def test_type_validate(self):
        """ Testing for getter validation """
        rect = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            stg = "{} must be > 0".format(attribute)
            # for invalid_type in self.invalid_types():
            #    print("Testing {}: {}".format(attribute, invalid_type))
            with self.assertRaises(ValueError) as err:
                if attribute in ["x", "y"]:
                    setattr(rect, attribute, -5)
                else:
                    setattr(rect, attribute, -(randrange(10) + 1))
                self.assertEqual(str(err.exception), stg)

    def test_validate_negative_gt(self):
        """ Testing for getter validation """
        rect = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            stg = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as err:
                setattr(rect, attribute, -(randrange(10) + 1))
            self.assertEqual(str(err.exception), stg)

    def test_validate_negative_ge(self):
        """ Testing for getter validation  """
        rect = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            stg = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as err:
                setattr(rect, attribute, -(randrange(10) + 1))
            self.assertEqual(str(err.exception), stg)

    def test_validate_zero(self):
        """ Testing for getter validation  """
        rect = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            stg = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as err:
                setattr(rect, attribute, 0)
            self.assertEqual(str(err.exception), stg)

    def test_getter(self):
        """ Testing for getter """
        rect = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            num = randrange(10) + 1
            setattr(rect, attribute, num)
            self.assertEqual(getattr(rect, attribute), num)

    def test_getter_range_zero(self):
        """ Testing for getter """
        rect = Rectangle(1, 2)
        rect.x = 0
        rect.y = 0
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_area_no_args(self):
        """ Testing for area() method  """
        rect = Rectangle(5, 6)
        with self.assertRaises(TypeError) as err:
            Rectangle.area()
        stg = (
                """area() missing 1 required """
                """positional argument: 'self'"""
                )
        self.assertEqual(str(err.exception), stg)

    def test_area(self):
        """ Testing for area() method compuation """
        rect = Rectangle(5, 7)
        self.assertEqual(rect.area(), 35)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rect.width = w
        rect.height = h
        self.assertEqual(rect.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rect = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(rect.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rect = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(rect.area(), w * h)

        rect1 = Rectangle(3, 2)
        self.assertEqual(rect1.area(), 6)

        rect2 = Rectangle(2, 10)
        self.assertEqual(rect2.area(), 20)

        rect3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect3.area(), 56)

    def test_display_no_args(self):
        """ Testing for display() method  """
        rect = Rectangle(9, 8)
        with self.assertRaises(TypeError) as err:
            Rectangle.display()
        stg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), stg)

    def test_str_no_args(self):
        """ Testing for __str__() method  """
        rect = Rectangle(5, 2)
        with self.assertRaises(TypeError) as err:
            Rectangle.__str__()
        stg = (
                """__str__() missing 1 required positional """
                """argument: 'self'"""
                )
        self.assertEqual(str(err.exception), stg)

    def test_str(self):
        """ Testing for __str__() method return """
        rect = Rectangle(5, 2)
        stg = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(rect), stg)
        rect = Rectangle(1, 1, 1)
        stg = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(rect), stg)
        rect = Rectangle(3, 4, 5, 6)
        stg = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(rect), stg)

        Base._Base__nb_objects = 0
        rect1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect1), "[Rectangle] (12) 2/1 - 4/6")

        rect2 = Rectangle(5, 5, 1)
        self.assertEqual(str(rect2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_no_args(self):
        """ Testing for update() method  """
        rect = Rectangle(5, 2)
        with self.assertRaises(TypeError) as err:
            Rectangle.update()
        stg = (
                """update() missing 1 required positional """
                """argument: 'self'"""
                )
        self.assertEqual(str(err.exception), stg)

        data = rect.__dict__.copy()
        rect.update()
        self.assertEqual(rect.__dict__, data)

    def test_update_args(self):
        """ Testing for update() postional args """
        rect = Rectangle(5, 2)
        data = rect.__dict__.copy()
        rect.update(10)
        data["id"] = 10
        self.assertEqual(rect.__dict__, data)
        rect.update(10, 5)
        data["_Rectangle__width"] = 5
        self.assertEqual(rect.__dict__, data)

        rect.update(10, 5, 17)
        data["_Rectangle__height"] = 17
        self.assertEqual(rect.__dict__, data)

        rect.update(10, 5, 17, 20)
        data["_Rectangle__x"] = 20
        self.assertEqual(rect.__dict__, data)

        rect.update(10, 5, 17, 20, 25)
        data["_Rectangle__y"] = 25
        self.assertEqual(rect.__dict__, data)

    def test_bad_args_update(self):
        """ Testing for update() positional arg fubars """
        rect = Rectangle(5, 2)
        data = rect.__dict__.copy()
        rect.update(10)
        data["id"] = 10
        self.assertEqual(rect.__dict__, data)
        with self.assertRaises(ValueError) as err:
            rect.update(10, -5)
        stg = "width must be > 0"
        self.assertEqual(str(err.exception), stg)
        with self.assertRaises(ValueError) as err:
            rect.update(10, 5, -17)
        stg = "height must be > 0"
        self.assertEqual(str(err.exception), stg)
        with self.assertRaises(ValueError) as err:
            rect.update(10, 5, 17, -20)
        stg = "x must be >= 0"
        self.assertEqual(str(err.exception), stg)
        with self.assertRaises(ValueError) as err:
            rect.update(10, 5, 17, 20, -25)
        stg = "y must be >= 0"
        self.assertEqual(str(err.exception), stg)

    def test_kwargs_update(self):
        """ Testing for update() keyword args """
        rect = Rectangle(5, 2)
        data = rect.__dict__.copy()
        rect.update(id=10)
        data["id"] = 10
        self.assertEqual(rect.__dict__, data)
        rect.update(width=5)
        data["_Rectangle__width"] = 5
        self.assertEqual(rect.__dict__, data)
        rect.update(height=17)
        data["_Rectangle__height"] = 17
        self.assertEqual(rect.__dict__, data)
        rect.update(x=20)
        data["_Rectangle__x"] = 20
        self.assertEqual(rect.__dict__, data)
        rect.update(y=25)
        data["_Rectangle__y"] = 25
        self.assertEqual(rect.__dict__, data)

    def test_kwargs_update2(self):
        """ Testing for update() keyword args """
        rect = Rectangle(5, 2)
        data = rect.__dict__.copy()
        rect.update(id=10)
        data["id"] = 10
        self.assertEqual(rect.__dict__, data)
        rect.update(id=10, width=5)
        data["_Rectangle__width"] = 5
        self.assertEqual(rect.__dict__, data)
        rect.update(id=10, width=5, height=17)
        data["_Rectangle__height"] = 17
        self.assertEqual(rect.__dict__, data)
        rect.update(id=10, width=5, height=17, x=20)
        data["_Rectangle__x"] = 20
        self.assertEqual(rect.__dict__, data)
        rect.update(id=10, width=5, height=17, x=20, y=25)
        data["_Rectangle__y"] = 25
        self.assertEqual(rect.__dict__, data)
        rect.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rect.__dict__, data)
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(height=1)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/1")
        rect1.update(width=1, x=2)
        self.assertEqual(str(rect1), "[Rectangle] (1) 2/10 - 1/1")
        rect1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rect1), "[Rectangle] (89) 3/1 - 2/1")
        rect1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rect1), "[Rectangle] (89) 1/3 - 4/2")
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(89)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 10/10")
        rect1.update(89, 2)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 2/10")
        rect1.update(89, 2, 3)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 2/3")
        rect1.update(89, 2, 3, 4)
        self.assertEqual(str(rect1), "[Rectangle] (89) 4/10 - 2/3")
        rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect1), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """ Testing for to_dictionary() method:"""
        with self.assertRaises(TypeError) as err:
            Rectangle.to_dictionary()
        stg = (
                """to_dictionary() missing 1 required """
                """positional argument: 'self'"""
                )
        self.assertEqual(str(err.exception), stg)

        rect = Rectangle(1, 2)
        data = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(rect.to_dictionary(), data)

        rect = Rectangle(1, 2, 3, 4, 5)
        data = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(rect.to_dictionary(), data)
        rect.x = 10
        rect.y = 20
        rect.width = 30
        rect.height = 40
        data = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(rect.to_dictionary(), data)
        rect1 = Rectangle(10, 2, 1, 9)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle(1, 1)
        rect2.update(**rect1_dictionary)
        self.assertEqual(str(rect1), str(rect2))
        self.assertNotEqual(rect1, rect2)

    def test_simple_display(self):
        """ Testing for display() method output """
        rect = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = "#\n"
        self.assertEqual(f.getvalue(), stg)
        rect.width = 3
        rect.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), stg)
        rect = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(f.getvalue(), stg)
        rect = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = """\
#########
#########
#########
#########
#########
#########
#########
#########
"""
        self.assertEqual(f.getvalue(), stg)
        rect = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = """\










          #
"""
        self.assertEqual(f.getvalue(), stg)

        rect = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), stg)

        rect = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = """\
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), stg)

        rect = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            rect.display()
        stg = """\




#####
#####
#####
"""
        self.assertEqual(f.getvalue(), stg)


if __name__ == "__main__":
    unittest.main()
