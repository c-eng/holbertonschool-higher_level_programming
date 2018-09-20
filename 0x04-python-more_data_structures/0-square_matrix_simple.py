#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    if matrix:
        for i in matrix:
            new.append(list(map(lambda list: list**2, i)))
    return new
