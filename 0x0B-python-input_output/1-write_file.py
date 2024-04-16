#!/usr/bin/python3
"""
module to write a string to a txt file
"""


def write_file(filename="", text=""):
    """
    Writing a string to a UTF8 txt file
    Args:
    filename (str): name of file
    test (str): text in file
    Return:number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
