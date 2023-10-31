#!/usr/bin/python3
"""
Title: Print square
Description: Write a function that prints a square with the character #
@a_idk scripting
"""


def print_square(size):
    """
    Method print_square definition
    Args:
        size: size of the square
    Raises:
        TypeError: size is not an int.
        ValueError: size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
