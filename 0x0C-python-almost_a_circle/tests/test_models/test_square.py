#!/usr/bin/python3
"""
Title: Python Unittest suites for square.py
Description: creating the test suites for use with square.py
@a_idk scripting
"""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """
    Test case suite for Square class
    """

    def setUp(self):
        """ Imports module, instantiates class """
        Base._Base__nb_objects = 0

    def test_squareclass(self):
        """ Testing for the class type """
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_inheritance(self):
        """ Testing for Square inherits Base """
        self.assertTrue(issubclass(Square, Base))

    def test_ARGS_initializator(self):
        """ Testing for many arguments initialization """
        with self.assertRaises(TypeError) as err:
            shape = Square(1, 2, 3, 4, 5)
        stg = "__init__() takes from 1 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(err.exception), stg)

    def test_instance(self):
        """ Testing for instantiation """
        shape = Square(10)
        self.assertEqual(str(type(shape)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(shape, Base))
        data = {'_Rectangle__height': 10, '_Rectangle__width': 10,
                '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(shape.__dict__, data)

        with self.assertRaises(TypeError) as err:
            shape = Square("5")
        message = "width must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(TypeError) as err:
            shape = Square(2, "7")
        message = "x must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(TypeError) as err:
            shape = Square(2, 5, "9")
        message = "y must be an integer"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            shape = Square(-2)
        message = "width must be > 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            shape = Square(1, -6)
        message = "x must be >= 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            shape = Square(1, 3, -7)
        message = "y must be >= 0"
        self.assertEqual(str(err.exception), message)

        with self.assertRaises(ValueError) as err:
            shape = Square(0)
        message = "width must be > 0"
        self.assertEqual(str(err.exception), message)

    def test_noARGS_initializator(self):
        """ Testing for initialization with no arg """
        with self.assertRaises(TypeError) as err:
            shape = Square()
        stg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(err.exception), stg)

    def test_position_instance(self):
        """ Testing for the positional instantiation """
        shape = Square(5, 10, 15)
        data = {'_Rectangle__height': 5, '_Rectangle__width': 5,
                '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(shape.__dict__, data)

        shape = Square(5, 10, 15, 20)
        data = {'_Rectangle__height': 5, '_Rectangle__width': 5,
                '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(shape.__dict__, data)

    def test_kwargs_instance(self):
        """ Testing for keyword instantiation """
        shape = Square(240, id=76, y=96, x=111)
        data = {'_Rectangle__height': 240, '_Rectangle__width': 240,
                '_Rectangle__x': 111, '_Rectangle__y': 96, 'id': 76}
        self.assertEqual(shape.__dict__, data)

    def test_F_properties(self):
        """ Testing property getters/setters """
        shape = Square(5, 9)
        shape.size = 98
        shape.x = 102
        shape.y = 103
        data = {'_Rectangle__height': 98, '_Rectangle__width': 98,
                '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(shape.__dict__, data)
        self.assertEqual(shape.size, 98)
        self.assertEqual(shape.x, 102)
        self.assertEqual(shape.y, 103)

    def invalid_types(self):
        """ Returns tuple of types for validation """
        tup = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
               [4], {5}, {6: 7}, None)
        return tup

    def test_inherited_class(self):
        """ Testing for inherited Base id """
        Base._Base__nb_objects = 98
        shape = Square(2)
        self.assertEqual(shape.id, 99)

    def test_valid_type(self):
        """ Testing the type validation """
        shape = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            stg = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as err:
                    setattr(shape, attribute, invalid_type)
                self.assertEqual(str(err.exception), stg)

        stg = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as err:
                setattr(shape, "width", invalid_type)
            self.assertEqual(str(err.exception), stg)

    def test_negative_gt_validation(self):
        """ Testing for greater than validation """
        shape = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            stg = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as err:
                setattr(shape, attribute, -(randrange(10) + 1))
            self.assertEqual(str(err.exception), stg)

    def test_validate_value_zero(self):
        """ Testing for property validation """
        shape = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            stg = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as err:
                setattr(shape, attribute, 0)
            self.assertEqual(str(err.exception), stg)

    def test_getter(self):
        """ Testing for setting/getting """
        shape = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(shape, attribute, n)
            self.assertEqual(getattr(shape, attribute), n)

    def test_negative_greater_equal_validatidation(self):
        """ Testing for greater than and equal to validation """
        shape = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            stg = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as err:
                setattr(shape, attribute, -(randrange(10) + 1))
            self.assertEqual(str(err.exception), stg)

    def test_getter_zero(self):
        """ Testing for setting/getting """
        shape = Square(1, 2)
        shape.y = 0
        shape.x = 0
        self.assertEqual(shape.x, 0)
        self.assertEqual(shape.y, 0)

    def test_no_args_area(self):
        """ Testing for area() method """
        shape = Square(5)
        with self.assertRaises(TypeError) as err:
            Square.area()
        stg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), stg)

    def test_no_arg_disp(self):
        """ Testing display() """
        shape = Square(9)
        with self.assertRaises(TypeError) as err:
            Square.display()
        stg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), stg)

    def test_simple_disp(self):
        """ Testing for display() method output """
        shape = Square(1)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = "#\n"
        self.assertEqual(fd.getvalue(), stg)
        shape.size = 3
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(fd.getvalue(), stg)
        shape = Square(5, 6, 7)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(fd.getvalue(), stg)
        shape = Square(9, 8)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(fd.getvalue(), stg)
        shape = Square(1, 1, 10)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\










 #
"""
        self.assertEqual(fd.getvalue(), stg)
        shape = Square(5)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(fd.getvalue(), stg)

        shape = Square(5, 5)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(fd.getvalue(), stg)
        shape = Square(5, 3)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(fd.getvalue(), stg)

        shape = Square(5, 0, 4)
        fd = io.StringIO()
        with redirect_stdout(fd):
            shape.display()
        stg = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(fd.getvalue(), stg)

        Base._Base__nb_objects = 0
        sqr1 = Square(5)
        self.assertEqual(str(sqr1), "[Square] (1) 0/0 - 5")
        self.assertEqual(sqr1.area(), 25)
        fd = io.StringIO()
        with redirect_stdout(fd):
            sqr1.display()
        stg = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(fd.getvalue(), stg)

        sqr2 = Square(2, 2)
        self.assertEqual(str(sqr2), "[Square] (2) 2/0 - 2")
        self.assertEqual(sqr2.area(), 4)
        fd = io.StringIO()
        with redirect_stdout(fd):
            sqr2.display()
        stg = """\
  ##
  ##
"""
        self.assertEqual(fd.getvalue(), stg)
        sqr3 = Square(3, 1, 3)
        self.assertEqual(str(sqr3), "[Square] (3) 1/3 - 3")
        self.assertEqual(sqr3.area(), 9)
        fd = io.StringIO()
        with redirect_stdout(fd):
            sqr3.display()
        stg = """\



 ###
 ###
 ###
"""
        self.assertEqual(fd.getvalue(), stg)

    def test_arg_area(self):
        """ Testing for area() compuation """
        shape = Square(6)
        self.assertEqual(shape.area(), 36)
        w = randrange(10) + 1
        shape.size = w
        self.assertEqual(shape.area(), w * w)
        w = randrange(10) + 1
        shape = Square(w, 7, 8, 9)
        self.assertEqual(shape.area(), w * w)
        w = randrange(10) + 1
        shape = Square(w, y=7, x=8, id=9)
        self.assertEqual(shape.area(), w * w)

        Base._Base__nb_objects = 0
        sqr1 = Square(5)
        self.assertEqual(str(sqr1), "[Square] (1) 0/0 - 5")
        self.assertEqual(sqr1.size, 5)
        sqr1.size = 10
        self.assertEqual(str(sqr1), "[Square] (1) 0/0 - 10")
        self.assertEqual(sqr1.size, 10)

        with self.assertRaises(TypeError) as err:
            sqr1.size = "9"
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(ValueError) as err:
            sqr1.size = 0
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_noArgs_str_(self):
        """ Testing __str__() """
        shape = Square(5, 2)
        with self.assertRaises(TypeError) as err:
            Square.__str__()
        stg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), stg)

    def test__str(self):
        """ Testing for __str__() method """
        shape = Square(5)
        stg = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(shape), stg)
        shape = Square(1, 1)
        stg = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(shape), stg)
        shape = Square(3, 4, 5)
        stg = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(shape), stg)
        shape = Square(10, 20, 30, 40)
        stg = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(shape), stg)

    def test_update(self):
        """ Testing for update() postional args """
        shape = Square(5, 2)
        data = shape.__dict__.copy()

        shape.update(10)
        data["id"] = 10
        self.assertEqual(shape.__dict__, data)

        shape.update(10, 5)
        data["_Rectangle__height"] = 5
        data["_Rectangle__width"] = 5
        self.assertEqual(shape.__dict__, data)

        shape.update(10, 5, 20)
        data["_Rectangle__x"] = 20
        self.assertEqual(shape.__dict__, data)

        shape.update(10, 5, 20, 25)
        data["_Rectangle__y"] = 25
        self.assertEqual(shape.__dict__, data)

    def test_bad_update(self):
        """ Testing for positional arg update() """
        shape = Square(5, 2)
        data = shape.__dict__.copy()

        shape.update(10)
        data["id"] = 10
        self.assertEqual(shape.__dict__, data)

        with self.assertRaises(ValueError) as err:
            shape.update(10, -5)
        stg = "width must be > 0"
        self.assertEqual(str(err.exception), stg)

        with self.assertRaises(ValueError) as err:
            shape.update(10, 5, -17)
        stg = "x must be >= 0"
        self.assertEqual(str(err.exception), stg)

        with self.assertRaises(ValueError) as err:
            shape.update(10, 5, 17, -25)
        stg = "y must be >= 0"
        self.assertEqual(str(err.exception), stg)

    def test_noArgs_update(self):
        """ Testing for update() """
        shape = Square(5, 2)
        with self.assertRaises(TypeError) as err:
            Square.update()
        stg = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), stg)

        data = shape.__dict__.copy()
        shape.update()
        self.assertEqual(shape.__dict__, data)

    def test_kwargs_update(self):
        """ Testing for kwargs update """
        shape = Square(5, 2)
        data = shape.__dict__.copy()

        shape.update(id=10)
        data["id"] = 10
        self.assertEqual(shape.__dict__, data)

        shape.update(size=17)
        data["_Rectangle__height"] = 5 
        data["_Rectangle__width"] = 17
        self.assertEqual(shape.__dict__, data)

        shape.update(x=20)
        data["_Rectangle__x"] = 20
        self.assertEqual(shape.__dict__, data)

        shape.update(y=25)
        data["_Rectangle__y"] = 25
        self.assertEqual(shape.__dict__, data)

    def test_kwargs_update2(self):
        """ Testing for kwargs update() """
        shape = Square(5, 2)
        data = shape.__dict__.copy()

        shape.update(id=10)
        data["id"] = 10
        self.assertEqual(shape.__dict__, data)

        shape.update(id=10, size=5)
        data["_Rectangle__height"] = 5
        data["_Rectangle__width"] = 5
        self.assertEqual(shape.__dict__, data)

        shape.update(id=10, size=5, x=20)
        data["_Rectangle__x"] = 20
        self.assertEqual(shape.__dict__, data)

        shape.update(id=10, size=5, x=20, y=25)
        data["_Rectangle__y"] = 25
        self.assertEqual(shape.__dict__, data)

        shape.update(y=25, id=10, x=20, size=5)
        self.assertEqual(shape.__dict__, data)

        Base._Base__nb_objects = 0
        sqr1 = Square(5)
        self.assertEqual(str(sqr1), "[Square] (1) 0/0 - 5")

        sqr1.update(10)
        self.assertEqual(str(sqr1), "[Square] (10) 0/0 - 5")

        sqr1.update(1, 2)
        self.assertEqual(str(sqr1), "[Square] (1) 0/0 - 2")

        sqr1.update(1, 2, 3)
        self.assertEqual(str(sqr1), "[Square] (1) 3/0 - 2")

        sqr1.update(1, 2, 3, 4)
        self.assertEqual(str(sqr1), "[Square] (1) 3/4 - 2")

        sqr1.update(x=12)
        self.assertEqual(str(sqr1), "[Square] (1) 12/4 - 2")

        sqr1.update(size=7, y=1)
        self.assertEqual(str(sqr1), "[Square] (1) 12/1 - 7")

        sqr1.update(size=7, id=89, y=1)
        self.assertEqual(str(sqr1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """ Testing to_dictionary() method """
        with self.assertRaises(TypeError) as err:
            Square.to_dictionary()
        stg = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), stg)

        shape = Square(1)
        data = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(shape.to_dictionary(), data)

        shape = Square(9, 2, 3, 4)
        data = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(shape.to_dictionary(), data)

        shape.x = 10
        shape.y = 20
        shape.size = 30
        data = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(shape.to_dictionary(), data)

        sqr1 = Square(10, 2, 1)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square(1, 1)
        sqr2.update(**sqr1_dictionary)
        self.assertEqual(str(sqr1), str(sqr2))
        self.assertNotEqual(sqr1, sqr2)

    def tearDown(self):
        """Cleans up after each test_method """
        pass


if __name__ == "__main__":
    unittest.main()
