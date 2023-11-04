#!/usr/bin/python3
"""
Title: Divide a matrix
Description: Write a function that divides all elements of a matrix
@a_idk scripting
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    Args:
        matrix: list of lists of integers or floats.
        div: divisor.
    Raises:
        TypeError: when matrix contains non-numbers, div not number,
                matrix contains rows of different sizes.
        ZeroDivisionError: the value of div is 0 (div == 0)
    """
    matrix_new = []  # initializing list
    tmp = []
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a \
                matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if len(matrix) is 0:
        raise TypeError("matrix must be a \
                matrix (list of lists) of integers/floats")
    elif len(matrix) is 1:
        for x in matrix[0]:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a \
                        matrix (list of lists) of integers/floats")
            tmp.append(float("{:.2f}".format(x / div)))
        matrix_new.append(tmp)
        return matrix_new
    else:
        length = len(matrix[0])
        for i in matrix:
            if not isinstance(i, list):
                raise TypeError("matrix must be a \
                        matrix (list of lists) of integers/floats")
            if len(i) != length:
                raise TypeError("Each row of the matrix \
                        must have the same size")
            for n in i:
                if type(n) not in [int, float]:
                    raise TypeError("matrix must be a \
                            matrix (list of lists) of integers/floats")
                tmp.append(float("{:.2f}".format(n / div)))
            matrix_new.append(tmp)
            tmp = []
        return (matrix_new)
