#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    if len(tuple_first) < 2:
        if len(tuple_first) == 0:
            tuple_first = 0, 0
        else:
            tuple_first = tuple_first[0], 0
            if len(tuple_snd) < 2:
                if len(tuple_snd) == 0:
                    tuple_snd = 0, 0
                else:
                    tuple_snd = tuple_snd[0], 0

                    return (tuple_first[0] + tuple_snd[0], tuple_first[1] + tuple_snd[1])
