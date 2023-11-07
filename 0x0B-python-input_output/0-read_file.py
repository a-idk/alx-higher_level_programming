#!/usr/bin/python3
"""
Title: Read file
Description: Write a function that reads a text file (UTF8) and prints
    it to stdout
@a_idk scripting
"""


def read_file(filename=""):
    """
    Method that reads a file with UTF-8 format
    """

    with open(filename, 'r', encoding="utf-8") as f:
        # with autocloses after suite finishes
        print(f.read(), end="")
