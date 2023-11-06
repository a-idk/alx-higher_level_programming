#!/usr/bin/python3
"""
Title: Exact same object
Description: function(method) that returns True if the object is exactly
        an instance of the specified class ; otherwise False
@a_idk Scripting
"""


def is_same_class(obj, a_class):
    """ Method that checks for exact same object """
    return (type(obj) == a_class)
