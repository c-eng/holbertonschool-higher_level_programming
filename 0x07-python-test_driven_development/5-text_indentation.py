#!/usr/bin/python3
"""
Documentation for text indentation function
"""


def text_indentation(text):
    """prints test while newlining (\n) twice upon certain characters
    (., :, ?).  Also strips whitespace before and after each discreet line.

    Args:
        text (str): test to parse
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    endline = 1
    a = ""
    for i in range(len(text)):
        if endline is 1 and text[i] is not ' ':
            a += text[i]
            endline = 0
        elif endline is 0:
            a += text[i]
        if (text[i] is ':' or text[i] is '.' or
           text[i] is '?'or text[i] is '\n'):
            print(a.strip(), end='')
            print()
            if text[i] is not '\n':
                print()
            a = ""
            endline = 1
    print(a.strip(), end='')
