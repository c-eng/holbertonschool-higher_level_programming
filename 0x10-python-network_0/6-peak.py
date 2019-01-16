#!/usr/bin/python3
"""find_peak function"""


def find_peak(peak_list):
    """finds peak
    Args:
        peak_list (list): list to find peaks in
    """
    lin = len(peak_list)
    if lin < 1:
        return None
    if lin < 2:
        return peak_list[0]
    mindex = int(lin / 2 - 1)
    if ((peak_list[mindex] >= peak_list[mindex + 1]) and
        (peak_list[mindex] >= peak_list[mindex - 1])):
        return peak_list[mindex]
    if (peak_list[mindex + 1] >= peak_list[mindex - 1]):
        return find_peak(peak_list[(mindex + 1):])
    else:
        return find_peak(peak_list[:(mindex - 1)])
