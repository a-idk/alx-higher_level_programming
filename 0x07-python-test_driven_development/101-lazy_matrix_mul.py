#!/usr/bin/python3
"""
Title: Lazy matrix multiplication
Description: Write a function that multiplies 2 matrices
            by using the module NumPy
@a_idk scripting
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Method lazy_matrix_mul definition
    Returns m_a * m_b
    Args:
        m_a: first matrix
        m_b: second matrix
    """
    return (numpy.matmul(m_a, m_b))
