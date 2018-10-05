#!/usr/bin/python3
"""
Documentation for matrix dividing function
"""


def matrix_divided(matrix, div):
    """Divides values in matrix against div.

    Args:
        matrix (:obj: list of :obj: list of :obj: int): matrix of numbers
        div (int or float): divisor
    """
    list_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(list_error)
    elif len(matrix) is 0:
        raise TypeError(list_error)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    count = len(matrix[0])
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(list_error)
        if len(matrix[i]) is 0:
            raise TypeError(list_error)
        if len(matrix[i]) is not count:
            raise TypeError("Each row of the matrix must have the same size")
        insert_matrix = []
        for j in range(len(matrix[i])):
            if not (isinstance(matrix[i][j], int) or
                    isinstance(matrix[i][j], float)):
                raise TypeError(list_error)
            insert_matrix.append(float('%.2f' % (matrix[i][j] / div)))
        new_matrix.append(insert_matrix)
    return new_matrix
