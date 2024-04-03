#!/usr/bin/python3

"""Define a class square"""


class Square:

    """Creates the properties that represent a square"""


def __init__(self, size=0):
    """Creates a new square
    Args: size of square (int)"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self._size = size

    def area(self):
        """Works out the area of a square"""

        return self._size ** 2
