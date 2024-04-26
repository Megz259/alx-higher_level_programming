#!/usr/bin/python3
"""
Module for defining a base class
"""


import json
from json import dumps, loads
import csv


class Base:
    """
    creating a class called base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of a string"""
        if list_dictionaries is None:
            return "[]"
        elif list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)

        return to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes list objects to a file"""
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                    jsonfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        """JSON representation of sting"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
