#!/usr/bin/python3
"""
Module that creates a script that reads stdin line by line and computes metrics
"""


def print_stats(f_size, status_int):
    """Printing metrics
    Args:
    f_size (int): file size
    status_int (dict): total of int"""
    print("File size:{}".format(f_size))
    for key in sorted(status_int):
        print("{}:{}".format(key, status_int[key]))

        if __name__ == "__main__":
            import sys

            f_size = 0
            status_int = {}
            p_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
            count = 0

            try:
                for line in sys.stdin:
                    if count == 10:
                        print_s(f_size, status_int)
                        count = 1
                    else:
                        count += 1

                        line = line.split()

                        try:
                            size += int(line[-1])
                            except (IndexError, ValueError):
                                pass

                            try:
                                if line[-2] in p_codes:
                                    if status_int.get(line[-2], -1) == -1:
                                        status_int[line[-2]] = 1
                                    else:
                                        status_int[line[-2]] += 1
                                        except IndexError:
                                            pass

                                        print_s(f_size, status_int)

                                        except KeyboardInterrupt
                                        print_s(f_size, status_int)
                                        raise
