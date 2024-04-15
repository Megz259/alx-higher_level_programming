#!/usr/bin/python3
"""
module with method is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if objects in a class are the same
    Args:
    obj: object to check
    a_class: class in question
    Returns:
    True if the object is exactly an instance of the specified class.
    otherwise False
    """

    if type(obj) == a_class:
        return True
    return False
