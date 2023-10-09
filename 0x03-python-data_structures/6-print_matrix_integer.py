#!/usr/bin/python3
# @a_idk scripting

# function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{:d}".format(y), end=" " if y != x[-1] else "")
        print()
