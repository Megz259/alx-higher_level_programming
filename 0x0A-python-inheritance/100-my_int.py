#!/usr/bin/python3

"""
module with class MyInt
"""


class MyInt(int):
    """To invert int operators"""

    def __ed__(self, value):
        """overriding operators"""
        return self.real != value

    def __ne__(self, value):
        """overriding operators"""
        return self.real == value
