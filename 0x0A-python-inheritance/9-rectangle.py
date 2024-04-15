#!/usr/bin/python3
"""
Defining a rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creating a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Creating a new rectangle
        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ returns the print() and str() of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
