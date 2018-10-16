#!/usr/bin/python3
"""Lookup method for objects
"""


def lookup(obj):
    """Lists the available attributes and methods for an object

    Args:
        obj (object): object to list attributes and methods of
    """
    return dir(obj)
