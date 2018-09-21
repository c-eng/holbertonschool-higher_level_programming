#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if type(roman_string) == str:
        for i in roman_string:
            if i == 'M':
                num += 1000
            elif i == 'D':
                num += 500
            elif i == 'C':
                num += 100
            elif i == 'L':
                num += 50
            elif i == 'X':
                num += 10
            elif i == 'V':
                num += 5
            elif i == 'I':
                num += 1
                if roman_string.find("CM") is not -1:
                    num -= 200
                if roman_string.find("CD") is not -1:
                    num -= 200
                if roman_string.find("XC") is not -1:
                    num -= 20
                if roman_string.find("XL") is not -1:
                    num -= 20
                if roman_string.find("IX") is not -1:
                    num -= 2
                if roman_string.find("IV") is not -1:
                    num -= 2
    return num
