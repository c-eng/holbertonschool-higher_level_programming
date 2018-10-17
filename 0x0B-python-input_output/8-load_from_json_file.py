#!/usr/bin/python3
"""Reads in JSON file and converts to a python object
"""
import json


def load_from_json_file(filename):
    """Reads in JSON document from a text file and deserializes it into a
       python object
    Args:
        filename (str): filename/filepath
    """
    if type(filename) is str:
        with open(filename, 'r') as fyle:
            return json.load(fyle)
