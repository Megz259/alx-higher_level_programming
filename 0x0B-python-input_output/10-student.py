#!/usr/bin/python3
"""
Module to write a class Student
"""


class Student:
    """creating class"""

    def __init__(self, first_name, last_name, age):
        """Creating student
        Args:
        first_name (str): first name
        last_name (str): last name
        age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """Dictionary representation
            Args:
            attrs (list): attributes
            """
            if attrs is None:
                return self.__dict__
            new_dict = {}
            for key, value in self.__dict__.items():
                if key is attrs:
                    new_dict[key] = value
                    return new_dict
