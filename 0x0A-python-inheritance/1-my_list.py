#!/usr/bin/python3
"""
module with class MyList
"""


class MyList(list):
    """Implements sorting method for printing"""

    def print_sorted(self):
    """Prints a list in ascending order"""

    print(sorted(self))
