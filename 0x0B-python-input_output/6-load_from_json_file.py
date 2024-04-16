#!/usr/bin/python3
"""
module that creates an object from JSON file
"""


import json


def load_from_json_file(filename):
    """
    creates an object from JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
