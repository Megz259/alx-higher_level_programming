#!/usr/bin/python3
"""
module with method is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is an instance or an inherited instance
    Args:
    obj: object to check
    a_class: class in question
    Returns:
    True if the object is an instance or an inherited instance.
    otherwise False
    """

    if isinstance(obj, a_class):
        return True
    return False
