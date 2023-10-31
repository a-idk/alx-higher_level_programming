#!/usr/bin/python3
"""
Title: Max integer - Unittest
Description: write unittests for the function
            def max_integer(list=[]):
@a_idk scripting
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class TestMaxInteger definition
    Args:
        test_one_element_list: Checks for input list with only 1 element
        test_ordered_list: Checks for ordered input list
        test_unordered_list: Checks for unordered input list
        test_floats: Checks input list for floats
        test_ints_and_floats: Checks input list for floats and int
        test_max_at_beginning: Checks for max value at start of list
        test_empty_string: Checks input for empty string
        test_empty_list: Checks input list for empty list
        test_string: Checks input for a string
        test_list_of_strings: Checks input list for strings
        """

    def test_one_element_list(self):
        """
        Checks for input list with only 1 element
        """
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_ordered_list(self):
        """
        Checks for ordered input list
        """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """
        Checks for unordered input list
        """
        unordered = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_floats(self):
        """
        Checks input list for floats
        """
        floats = [2.53, 6.33, -9.123, 16.2, 6.0]
        self.assertEqual(max_integer(floats), 16.2)

    def test_ints_and_floats(self):
        """
        Checks input list for a mix of floats and int
        """
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_max_at_begginning(self):
        """
        Checks for max value at start of list
        """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_string(self):
        """
        Checks input for empty string
        """
        self.assertEqual(max_integer(""), None)

    def test_empty_list(self):
        """
        Checks input list for empty list
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_string(self):
        """
        Checks input for a string
        """
        strg = "Dave"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """
        Checks input list for strings
        """
        strg = ["Dave", "is", "a", "boy"]
        self.assertEqual(max_integer(strg), "boy")


if __name__ == '__main__':
    unittest.main()
