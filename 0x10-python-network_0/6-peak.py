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
    mindex0 = peak_list[mindex]
    mindex1 = peak_list[mindex + 1]
    mindex2 = peak_list[mindex - 1]
    if ((mindex0 >= mindex1) and
        (mindex0 >= mindex2)):
        return mindex0
    if (mindex2 >= mindex1):
        return find_peak(peak_list[:mindex])
    else:
        return find_peak(peak_list[mindex + 1:])
