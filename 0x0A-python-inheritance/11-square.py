#!/usr/bin/python3
"""
module with class square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creating a square"""

    def __init__(self, size):
        """
        creating a square
        Args:
        size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""

        return self.__size ** 2

    def __str__(self):
        """returns print() and str() of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
