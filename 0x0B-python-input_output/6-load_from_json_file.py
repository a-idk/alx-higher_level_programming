#!/usr/bin/python3
"""
Title: Create object from a JSON file
Description: Write a function that creates an Object from a “JSON file”
@a_idk scripting
"""
import json


def load_from_json_file(filename):
    """
    Method that writes a function that creates an object from "JSON file"
    Args:
        filename: the file to be written to
    """
    with open(filename) as f:
        # with autocloses after suite finishes
        return json.load(f)
