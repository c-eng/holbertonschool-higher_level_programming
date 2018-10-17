#!/usr/bin/python3
"""read_file function
"""


def read_file(filename=""):
    """Reads a file
    Args:
        filename (str): filename/filepath
    """
    if type(filename) is str:
        with open(filename, 'r') as fyle:
            print(fyle.read(), end='')
