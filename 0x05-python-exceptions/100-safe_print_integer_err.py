#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        print("Exception:{:d}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
