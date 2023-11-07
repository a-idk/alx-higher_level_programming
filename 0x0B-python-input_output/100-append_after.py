#!/usr/bin/python3
"""
Title: Search and update
Description: Write a function that inserts a line of text to a file,
    after each line containing a specific string
@a_idk scripting
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Method that inserts a line of text to a file, after each line
    containing a specific string
    Args:
        search_string: searches the string
        new_string: string to be inserted
        filename: name of the file
    """
    # initializing text
    new_text = ""
    with open(filename) as f:
        for chars in f:
            new_text = new_text + chars
            if search_string in chars:
                new_text = new_text + new_string
    with open(filename, "w") as fw:
        fw.write(new_text)
