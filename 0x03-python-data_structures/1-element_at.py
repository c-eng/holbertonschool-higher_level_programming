#!/usr/bin/python3
def element_at(my_list, idx):
    if -1 < idx < len(my_list):
        return my_list[idx]
    else:
        return None
