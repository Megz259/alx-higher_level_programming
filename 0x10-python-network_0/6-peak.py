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
    
    top_i = None
    for element in list_of_integers:
        if top_i is None or top_i < element:
            top_i = element
            return top_i
