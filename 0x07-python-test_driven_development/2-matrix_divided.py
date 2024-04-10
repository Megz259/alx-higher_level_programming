#!/usr/bin/python3
""" Defining a division function"""


def matrix_divided(matrix, div):
    """dividing elements of a matrix
    Arguments:
    Matrix - lists if integeres and floats
    Div - division

    Return:
    TypeErrors for:
    matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must have the same size
    div must be a number
    division by zero
    Else:
    New matrix that has been divided"""
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of "
        "integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
        "integers/floats")
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
            "integers/floats")
        if len(lists) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of "
            "integers/floats")
        for items in lists:
            if not isintance(item, int) and not isinstance(item, float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

                if not all(len(row) == len(matrix[0]) for row in matrix):
                    raise TypeError("Each row of the matrix must have "
                        "the same size")

                if not isinstance(div, int) and not isinstance(div, float):
                    raise TypeError("div must be a number")

                if div == 0:
                    raise ZeroDivisionError("division by zero")

                return[[round(item / div, 2) for item in lists] for lists in matrix]
