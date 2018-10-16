#!/usr/bin/python3
"""Checks if an objects is an instances of or inherets from a class
"""


def is_kind_of_class(obj, a_class):
    """Checks if an objects is an instances of or inherets from a class
    Args:
        obj (object): object to check
        a_class (type): class to check against
    """
    return isinstance(obj, a_class)
