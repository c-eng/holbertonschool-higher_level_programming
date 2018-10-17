#!/usr/bin/python3
"""string to JSON
"""
import json


def to_json_string(my_obj):
    """Convert an object (string) to its JSON representation
    Args:
        my_obj (str): object to return JSON representation of
    """
    return json.dumps(my_obj)
