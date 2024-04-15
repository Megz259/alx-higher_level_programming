#!/usr/bin/python3
"""
Module with class BaseGeometry
"""


class BaseGeometry:
    """creating an empty class"""

    def area(self):
        """calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validating a parameter as an integer
        Args:
        name (str):name of parameter
        value (int): parameter
        Raise:
        TypeError: if not an integer
        ValueError: if less than 0
        """
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
