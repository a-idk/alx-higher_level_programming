#!/usr/bin/python3
"""
Title: Can I?
Description: Write a function that adds a new attribute to an object
    if it’s possible
@a_idk Scripting
"""


def add_attribute(obj, attribute, value):
    """
    Method that adds new attribute to an object if possible
    Args:
        obj: object
        attribute: attribute to be added to the object
        value: The value of att.
    Raises:
        TypeError: If the attribute cannot be added to the object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
