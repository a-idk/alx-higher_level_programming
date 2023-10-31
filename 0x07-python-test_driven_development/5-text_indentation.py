#!/usr/bin/python3
"""
Title: Text indentation
Description: Write a function that prints a text with 2 new lines
            after each of these characters: ., ? and :
@a_idk scripting
"""


def text_indentation(text):
    """
    Method text_indentation definition
    Arg:
        text: the text string or message
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in ".:?":
        text = (i + "\n\n").join([j.strip(" ") for j in text.split(i)])

    print("{}".format(text), end="")
