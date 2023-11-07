#!/usr/bin/python3
"""
Title: Student to disk and reload
Description: Write a class Student that defines a student by:
    (based on 10-student.py)
@a_idk scripting
"""


class Student:
    """
    Class Student definition
    """

    def __init__(self, first_name, last_name, age):
    """
    initializing the class Student
    Args:
        first_name: first name of student
        last_name: last name of student
        age: age of student
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        """
        dictionary representation
        Args:
            attrs: list of strings
        """
        if attrs is None:
            return self.__dict__
        # initializing the dictionary
        dict = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                dict[key] = val
        return dict
       """ return (self.__dict__)"""

    def reload_from_json(self, json):
        """
         replaces all attributes of the Student instance
         """
        for key, val in json.items():
            setattr(self, key, val)
