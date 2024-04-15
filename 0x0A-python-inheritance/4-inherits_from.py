#!/usr/bin/python3
"""
module with method inherits_from
"""


def inherits_from(obj, a_class):
    """
    checks if object is an inherited instance
    Args:
    obj: object to check
    a_class: class in question
    Returns:
    True if the object is an inherited instance.
    otherwise False
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
