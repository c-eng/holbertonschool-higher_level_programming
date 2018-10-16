#!/usr/bin/python3
"""Checks if an object is an exact instance of a specified class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an exact instance of a specified class
    Args:
        obj (object): object to check
        a_class (type): class to check against
    """
    return type(obj) == a_class
