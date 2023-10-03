#!/usr/bin/python3

for chars in range(97, 123):
    if chr(chars) is not 'e' and chr(chars) is not 'q':
        print("{}".format(chr(chars)), end="")
