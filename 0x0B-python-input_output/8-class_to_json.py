#!/usr/bin/python3
"""
Module that writes a function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """returns dictionary description"""
    return vars(obj)
