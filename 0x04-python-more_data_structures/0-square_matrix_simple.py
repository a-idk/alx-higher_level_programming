#!/usr/bin/python3
# @a_idk scripting

# function that computes the square value of all integers of a matrix


def square_matrix_simple(matrix=[]):
    # initializing the matrix
    mat_square = matrix.copy()
    # main loop
    for idx in range(len(matrix)):
        mat_square[idx] = list(map(lambda num: num**2, matrix[idx]))
    return (mat_square)
