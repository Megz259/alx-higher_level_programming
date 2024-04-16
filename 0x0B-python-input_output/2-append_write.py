#!/usr/bin/python3
"""
module to appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    appending a string at end of text file
    Args:
    filename (str): name of file
    test (str): text in file
    Return:the number of characters added
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
