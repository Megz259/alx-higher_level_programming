#!/usr/bin/python3
"""
Defining a rectangular class
"""


class Rectangle:
    """
    Represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Creating a rectangle

        Args:
        width (int): width of rectangle
        height (int): heisght of rectangle
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """
            getting the width of the rectangle
            """

            return self._width

        @width.setter
        def width(self, value):
            """Args:
            value (int): widths of rectangle

            Attributes:
            _width (int): width of rectangle

            Raise:
            TypeError: if not and int
            ValueError: if less than 0
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

        @property
        def height(self):
            """
            getting the height of a rectangle
            """

            return self._height

        @height.setter
        def height(self, value):
            """Args:
            value (int): height of rectangle

            Attributes:
            _height (int): height of rectangle

            Raises:
            TypeError: if not an int
            ValueError: if less than 0
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
