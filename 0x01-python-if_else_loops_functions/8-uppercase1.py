#!/usr/bin/python3
# @a_idk scripting

''' function that gives uppercase characters
followed by a new line.'''


def uppercase(str):
    for chars in str:
        if chars >= 'a' and chars <= 'z':
            up_chars = chr(ord(chars) - 32)
        # output the corresponding value
        print("{}".format(up_chars), end="")
    # output the last space
    print("")
