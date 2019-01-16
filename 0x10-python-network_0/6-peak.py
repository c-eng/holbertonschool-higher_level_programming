#!/usr/bin/python3
"""find_peak function"""


def find_peak(peak_list):
    """finds peak
    Args:
        peak_list (list): list to find peaks in
    """
    if len(peak_list) < 1:
        return None
    if len(peak_list) < 2:
        return peak_list[0]
    if len(peak_list) < 3:
        if peak_list[0] >= peak_list[1]:
            return peak_list[0]
        else:
            return peak_list[1]
    if ((peak_list[int(len(peak_list) / 2)] >=
         peak_list[int(len(peak_list) / 2) + 1]) and
        (peak_list[int(len(peak_list) / 2)] >=
         peak_list[int(len(peak_list) / 2) - 1])):
        return peak_list[int(len(peak_list) / 2)]
    if (peak_list[int(len(peak_list) / 2) - 1] >=
       peak_list[int(len(peak_list) / 2) + 1]):
        return find_peak(peak_list[:int(len(peak_list) / 2)])
    else:
        return find_peak(peak_list[int(len(peak_list) / 2) + 1:])
