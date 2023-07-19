#!/usr/bin/python
"""function module"""


def print_square(size):
    """prints a square with character #"""

    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
