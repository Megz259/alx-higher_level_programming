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
            if (type(attrs) == list and
                    all(type(element) == str for element in attrs)):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
