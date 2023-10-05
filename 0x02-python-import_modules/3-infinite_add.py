#!/usr/bin/python3
# @a_idk scripting

if __name__ == "__main__":

    import sys

    # initializing the sums
    result = 0

    # looping thru
    for x in range(len(sys.argv) - 1):
        result = result + int(sys.argv[x + 1])

    # printing the result
    print("{}".format(result))
