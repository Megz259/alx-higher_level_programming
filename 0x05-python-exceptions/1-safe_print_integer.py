#!/usr/bin/python3

"""safe_print_integer - print any type of integer
@value: integer
return: True if value has been correctly printed"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except(ValueError):
        return(False)
