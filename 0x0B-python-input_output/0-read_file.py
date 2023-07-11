#!/usr/bin/python3
"""function module"""


def read_file(filename=""):
    """reads from a txt file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read())

    f.closed
