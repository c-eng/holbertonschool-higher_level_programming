#!/usr/bin/python3
"""Line counting function
"""


def number_of_lines(filename=""):
    """counts and returns number of lines in a file
    Args:
       filename (str): filename/filepath
    """
    count = 0
    if type(filename) is str:
        with open(filename, 'r') as fyle:
            while (fyle.readline() != ''):
                count += 1
    return count
