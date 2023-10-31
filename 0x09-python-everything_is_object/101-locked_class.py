#!/usr/bin/python3
"""
Title: 101-locked_class.py
Description: a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name
Author: @a_idk scripting
"""


class LockedClass:
    """
    Class LockedClass definition
    """
    __slots__ = ["first_name"]
