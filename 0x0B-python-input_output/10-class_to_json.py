#!/usr/bin/python3
"""dict of class
"""


def class_to_json(obj):
    """Returns the dictionary description of a class
    Args:
        obj (class): class
    """
    return obj.__dict__
