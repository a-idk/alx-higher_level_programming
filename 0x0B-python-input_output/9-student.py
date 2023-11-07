#!/usr/bin/python3
"""
Title: Student to JSON
Description: Write a class Student that defines a student by
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

    def to_json(self):
        """ dictionary representation """
        return (self.__dict__)
