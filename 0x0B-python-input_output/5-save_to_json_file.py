#!/usr/bin/python3
"""
module that writes an object to text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to text file
    """
    with open(filename, "w") as f:
        return json.dumps(my_obj, f)
