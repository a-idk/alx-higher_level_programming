#!/usr/bin/python3
# @a_idk scripting

''' function that prints uppercase characters
followed by a new line.'''


def uppercase(str):
    for chars in str:
        if ord(chars) >= 97 and ord(chars) <= 122:
            chars = chr(ord(chars) - 32)
        # print the corresponding value
        print("{}".format(chars). end="")
    # print the last space
    print("")
