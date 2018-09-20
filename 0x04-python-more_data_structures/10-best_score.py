#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return list(a_dictionary.keys())[list(a_dictionary.values()).index
                                         (max(sorted(a_dictionary.values())))]
    else:
        return None
