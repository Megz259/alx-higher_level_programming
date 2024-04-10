#!/usr/bin/python3
"""Defining a square function"""


def print_square(size):
    """prints a square with the character #
    Arguments:
    size - size of square
    Raise:
    type error is not and int
    value error if less than 0"""
    if not isinstnace(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        [print("#", end="") for x in range(size)]
        print("")
