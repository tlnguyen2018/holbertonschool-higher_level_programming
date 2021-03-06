#!/usr/bin/python3
"""
Matrix division
"""


def matrix_divided(matrix, div):
    """
    Matrix must be a list of lists of integers or floats, otherwise
    raise a TypeError exception with the message
    matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must be of the same size, otherwise
    raise a TypeError exception with the message
    Each row of the matrix must have the same size
    div must be a number (integer or float), otherwise
    raise a TypeError exception with the message div must be a number
    div cant be equal to 0, otherwise
    raise a ZeroDivisionError exception with the message division by zero
    All elements of the matrix should be divided by div, rounded to 2 decimal
    Returns a new matrix
    """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_row = []
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of list) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
        new_row = []
    return (new_matrix)
