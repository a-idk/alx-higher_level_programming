#!/usr/bin/python3
# @a_idk scripting


# declaring and initializing index variable
indx = 0

for chars in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(chars - indx)), end="")
    # toggling the value of indx between 0 and 32
    indx = 32 if indx == 0 else 0
