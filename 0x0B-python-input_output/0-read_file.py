#!/usr/bin/python3
"""
Module for read file function
"""


def read_file(filename=""):
    """Prints the content of UTF8 to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
