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
    matrix_new = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for idx in matrix:
        if not isinstance(idx, list) or len(idx) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(idx) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in idx:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    for i in matrix:
        new_row = []
        for x in i:
            # Perform the division and rounding
            result = round(x / div, 2)
            new_row.append(result)
        matrix_new.append(new_row)
    return matrix_new


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
