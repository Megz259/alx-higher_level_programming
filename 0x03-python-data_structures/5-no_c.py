#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string"""
    cpoy = [y for y in my_string if y != 'C' and y != 'c']
    return {"".join(cpoy))
