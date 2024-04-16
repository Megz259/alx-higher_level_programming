#!/usr/bin/python3
"""
module that returns an object
"""


import json


def from_json_string(my_str):
    """
    returns object representation of JSON string
    """
    return json.loads(my_str)
