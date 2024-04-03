#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """my_list - prints elements from a list"""
    """x - number of elements"""

    y = 0
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
        print()
        return (y)
    """returns the number of elements"""
