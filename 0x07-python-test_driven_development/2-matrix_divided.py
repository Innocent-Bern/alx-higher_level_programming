#!/usr/bin/python3
"""matrix division module"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    rtn_matrix = []
    for i in matrix:
        arr = []
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for x in i:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            arr.append(round(x / div, 2))
        rtn_matrix.append(arr)
    return rtn_matrix
