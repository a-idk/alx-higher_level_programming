#!/usr/bin/python3
# @a_idk scripting

# function that computes the square value of all integers of a
# matrix using map


def square_matrix_map(matrix=[]):
    return (list(map(lambda i: list(map(lambda j: j**2, i)), matrix)))
