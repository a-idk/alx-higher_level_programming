#!/usr/bin/python3
"""
Title: Save Object to a file
Description: Write a function that writes an Object to a text file,
    using a JSON representation
@a_idk scripting
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method that writes an object to a text file using json rep
    Args:
        my_obj: the object
        filename: the file to be written to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        # with autocloses after suite finishes
        json.dump(my_obj, f)
