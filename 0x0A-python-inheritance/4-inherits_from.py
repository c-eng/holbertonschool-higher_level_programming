#!/usr/bin/python3
"""Checks if an objects is an instances of or inherets from a class
"""


def inherits_from(obj, a_class):
    """Checks if an objects is an instances of or inherets from a class
    Args:
        obj (object): object to check
        a_class (type): class to check against
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
