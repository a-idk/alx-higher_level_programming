#!/usr/bin/python3
"""
Title: Pascal's Triangle
Description: Create a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal’s triangle of n
@a_idk scripting
"""


def pascal_triangle(n):
    """
    Method that returns a list of lists integer representing the Pascal
    triangle
    Args:
        n: reference integer number
    """
    # Returns an empty list if n <= 0
    if n <= 0:
        return []
    # initializing the triangle
    tri_angles = [[1]]
    while len(tri_angles) != n:
        set_t = tri_angles[-1]
        store = [1]
        for index in range(len(set_t) - 1):
            store.append(set_t[index] + set_t[index + 1])
        store.append(1)
        tri_angles.append(store)
    return tri_angles
