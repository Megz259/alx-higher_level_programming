#!/usr/bin/python3
"""
Module to write a script that adds all arguments to a Python list,
and then save them to a file
"""


import sys
import json
import os.path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

    for index in argv[1:]:
        json_list.append(index)

        save_to_json_file(json_list, filename)
