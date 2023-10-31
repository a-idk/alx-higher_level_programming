#!/usr/bin/python3
"""
Title: Matrix multiplication
Description: Write a function that multiplies 2 matrices
@a_idk scripting
"""


def matrix_mul(m_a, m_b):
    """
    Method matrix_mul definitiion
    Args:
        m_a: first matrix
        m_b: second matrix
    Raises:
        TypeError: If m_a or m_b are not lists or lists of lists
        TypeError: If m_a or m_b are not rectangular & contain non int/float
        ValueError: If m_a or m_b cant multiply or are empty lists/matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # initializing the attributes
    m_a_empty = False
    m_a_notrect = False
    m_a_notnum = False
    m_b_empty = False
    m_b_notrect = False
    m_b_notnum = False
    for x in m_a:
        if not isinstance(x, list):
            raise TypeError("m_a must be a list of lists")
        if len(x) != len(m_a[0]):
            m_a_notrect = True
        for num in x:
            if not isinstance(num, (int, float)):
                m_a_notnum = True
    for x in m_b:
        if not isinstance(x, list):
            raise TypeError("m_b must be a list of lists")
        if len(x) != len(m_b[0]):
            m_b_notrect = True
        for num in x:
            if not isinstance(num, (int, float)):
                m_b_notnum = True
    # raising exceptions
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")
    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")
    if m_a_notrect:
        raise TypeError("each row of m_a must should be of the same size")
    if m_b_notrect:
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    outcome = [[] for i in range(len(m_a))]
    for m in range(len(m_a)):
        for n in range(len(m_b[0])):
            ad = 0  # initializing c
            for o in range(len(m_b)):
                ad = ad + m_a[m][o] * m_b[o][n]
            outcome[m].append(ad)
    return outcome


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
