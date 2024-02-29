#!/usr/bin/python3
"""containes peak function"""


def find_peak(list_of_integers):
    """finds peak in unsorted list of integers"""
    ls = list_of_integer
    length = len(ls)
    if length == 0:
        return
    middle = length // 2
    if ((middle == length - 1 or ls[middle] >= ls[middle + 1])
            and (middle == 0 or ls[middle] >= ls[middle - 1])):
        return ls[middle]
    if (middle != length - 1 and ls[middle + 1] > ls[middle]):
        return find_peak(ls[middle + 1:])
    return find_peak(ls[:middle])
