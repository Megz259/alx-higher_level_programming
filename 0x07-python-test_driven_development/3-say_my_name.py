#!/usr/bin/python3
"""Function to print a name"""


def say_my_name(first_name, last_name=""):
    """Printing a name

    Arguments:
    first_name - the first name
    last_name - the surname

    Raise:
    error message if there is not a first
    and last name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
