#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers
    Args:
    list_of_integers: the list

    Returns:
    the integer or nothing
    """
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        middle = (low + high) // 2
        if list_of_integers[middle] <= list_of_integers[middle + 1]:
            low = middle + 1
            else:
                high = middle

    if not list_of_integers:
        return None

    return list_of_integers[low]
