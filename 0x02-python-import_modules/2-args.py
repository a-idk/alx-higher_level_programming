#!/usr/bin/python3
# @a_idk scripting

if __name__ == "__main__":

    import sys

    # counting the number of arguments
    num = len(sys.argv) - 1

    # conditions
    if num == 0:
        print("0 arguments.")
    elif num > 1:
        print("{} arguments:".format(num))
    else:
        print("1 argument:")

    # printing the respective arguments
    for x in range(num):
        print(f"{x + 1}: {sys.argv[x + 1]}")
        # print("{}: {}".format(x + 1, sys.argv[x + 1]))
