#!/usr/bin/python3
for char in list(map(chr, range(97, 123))):
    if char != 'e' and char != 'q':
        print(char, end='')
