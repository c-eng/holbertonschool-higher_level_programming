#!/usr/bin/python3
"""
Documentation for name saying function
"""
def say_my_name(first_name, last_name=""):
    """Prints a name

    Args:
        first_name (str): first name
        last_name (str): last name

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
