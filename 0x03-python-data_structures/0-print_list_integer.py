#!/usr/bin/python3
#0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Print all integers of a list"""
    for x in range(len(my_list)):
        print(f"{my_list[x]:d}")
