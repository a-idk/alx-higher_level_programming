#!/usr/bin/python3
"""
Title: Class to JSON
Description: Write a function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and
    boolean) for JSON serialization of an object
@a_idk scripting
"""


def class_to_json(obj):
    """
    Method that returns dict description for JSON serialized object
    Args:
        object: instance of a CLass that is serialized
    """
    return obj.__dict__
    """ return vars(obj)"""
