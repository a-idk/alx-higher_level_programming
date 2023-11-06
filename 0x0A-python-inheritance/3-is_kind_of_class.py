#!/usr/bin/python3
"""
Title: ESame class or inherit from
Description: function(method) that returns True if the object is an
        instance of, or if the object is an instance of a class that
        inherited from, the specified class ; otherwise False
@a_idk Scripting
"""


def is_kind_of_class(obj, a_class):
    """ Method that checks for same class or inherit from """
    return (isinstance(obj, a_class))
