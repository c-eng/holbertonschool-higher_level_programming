#!/usr/bin/python3
"""
Documentation for square printing function
"""
def print_square(size):
    """Prints a square using the '#' character

    Args:
        size (int): size of the square to print
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    if size is 0:
        print()
