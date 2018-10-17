#!/usr/bin/python3
"""Read n lines function
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines from a file
    Args:
        filename (str): filename/filepath
        nb_lines (int): numbr of lines to read
    """
    count = 0
    if type(nb_lines) is int and type(filename) is str:
        with open(filename) as fyle:
            while (count < nb_lines or nb_lines <= 0):
                read = fyle.readline()
                if read == '':
                    break
                print(read, end='')
                count += 1
