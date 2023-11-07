#!/usr/bin/python3
"""
Title: Write to file
Description: Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written
@a_idk scripting
"""


def write_file(filename="", text=""):
    """
    Method that reads a file with UTF-8 format
    Args:
        filename: name of the file to be written to
        text: string to be written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        # with autocloses after suite finishes
        return (f.write(text))
