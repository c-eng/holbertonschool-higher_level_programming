#!/usr/bin/python3
"""Pascal Triangle function
"""


def pascal_triangle(n):
    """Pascals Triangle
    """
    new = []
    for i in range(n):
        add = [1]
        if i > 0:
            for j in range(len(new[i - 1])):
                if j == len(new[i - 1]) - 1:
                    add.append(1)
                else:
                    add.append(new[i - 1][j] + new[i - 1][j + 1])
        new.append(add)
    return new
