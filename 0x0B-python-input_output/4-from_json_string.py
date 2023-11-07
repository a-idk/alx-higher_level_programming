#!/usr/bin/python3
"""
Title: From JSON string to Object
Description: Write a function that returns an object (Python data
    structure) represented by a JSON string
@a_idk scripting
"""
import json


def from_json_string(my_str):
    """
    Method that writes a function that returns an object (Python data
    structure) represented by a JSON string
    Args:
        my_str: json string
    """

    return (json.loads(my_str))
