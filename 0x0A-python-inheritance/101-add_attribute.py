#!/usr/bin/python3
"""
module to add new attribute to object
"""


def add_attribute(obj, att, value):
    """
    adding an attribute
    Args:
    obj: object
    att: attributes
    value: value
    Raise:
    TypeError can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
