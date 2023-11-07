#!/usr/bin/python3
"""
Title: To JSON string
Description: Write a function that returns the JSON representation of
    an object (string)
@a_idk scripting
"""
import json


def to_json_string(my_obj):
    """
    Method that writes a function that returns JSON rep of an object
    Args:
        my_obj: the object
    """

    return (json.dumps(my_obj))
