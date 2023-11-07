#!/usr/bin/python3
"""
Title: Append to a file
Description: Write a function that appends a string to a text file (UTF8)
    and returns the number of characters written
@a_idk scripting
"""


def append_write(filename="", text=""):
    """
    Method that appends a text to file with UTF-8 format
    Args:
        filename: name of the file to be written to
        text: string to be written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        # with autocloses after suite finishes
        return (f.write(text))
