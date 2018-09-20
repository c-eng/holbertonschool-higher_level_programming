#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for k, v in a_dictionary.items():
        b_dictionary[k] = v * 2
    return b_dictionary
