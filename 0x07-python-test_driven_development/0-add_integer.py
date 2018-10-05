#!/usr/bin/python3
"""
Documentation for integer adding function
"""


def add_integer(a, b=98):
    """add_integer function: adds two integers and
    converts float to int if necessary

    Args:
        a (int): first value to add
        b (int): second value to add, default 98
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
