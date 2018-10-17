#!/usr/bin/python3
"""Save python object to file in JSON format
"""
import json


def save_to_json_file(my_obj, filename):
    """Converts Python object to JSON format and writes it to a text file
    Args:
        my_obj (obj): object to convert
        filename (str): filename/filepath
    """
    if type(filename) is str:
        with open(filename, 'w') as fyle:
            json.dump(my_obj, fyle)
