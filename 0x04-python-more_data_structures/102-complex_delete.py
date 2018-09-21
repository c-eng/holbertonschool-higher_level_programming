#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kee = []
    for k, v in a_dictionary.items():
        if v == value:
            kee.append(k)
    for k in kee:
        del a_dictionary[k]
    return a_dictionary
