#!/usr/bin/python3

"""safe_print_list_integers- prints the first x elements of a
list and only integers.
@my_list: list to print from
@x: integer
return: Returns the real number of integers printed"""


def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for x in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            y += 1
        except(ValueError, TypeError):
            continue
        print()
        return (y)
