#!/usr/bin/python3
"""Appends text to a file
"""


def append_write(filename="", text=""):
    """Appends text to filename
    Args:
        filename (str): filename/filepath
        text (str): text to append
    """
    if type(filename) is str and type(text) is str:
        with open(filename, 'a') as fyle:
            count = fyle.write(text)
    return count
