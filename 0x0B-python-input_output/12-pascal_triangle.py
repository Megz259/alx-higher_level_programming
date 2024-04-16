#!/usr/bin/python3
"""
Function that that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """triangle of n size"""
    pt = []
    if n <= 0:
        return pt
    for j in range(n):
        pt_a = []
        pt_a.append(1)
        if j == 0:
            pt.append(pt_a)
            continue
        for k in range(1, j):
            try:
                pt_a.append(pt[j - 1][k - 1] + pt[j - 1][k])
            except:
                continue
            pt_a.append(1)
            pt.append(pt_a)

            return pt
