#!/usr/bin/python3
"""
Title: Integers addition
Description: Write a function that adds 2 integers
@a_idk scripting
"""


def add_integer(a, b=98):
    """
    Returns sum (int) of a and b,
    Args:
        a: the first number
        b: the second number
    Raises:
        TypeError
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
