#!/usr/bin/python3
"""deserializes JSON document to Python object
"""
import json


def from_json_string(my_str):
    """Converts my_str string from JSON document to python object
    Args:
        my_str (str): JSON document string
    """
    return json.loads(my_str)
