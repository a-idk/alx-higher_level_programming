#!/usr/bin/python3
# @a_idk scripting

''' function that gives uppercase characters
followed by a new line.'''


def uppercase(str):
    for chars in str:
        if ord(chars) >= 97 and ord(chars) <= 122:
            chars = chr(ord(chars) - 32)
        # output the corresponding value
        print("{}".format(chars). end="")
    # output the last space
    print("")
