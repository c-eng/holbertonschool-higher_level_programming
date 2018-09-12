#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ''
    for ind in range(len(str)):
        if ind != n:
            temp += str[ind]
    return temp
