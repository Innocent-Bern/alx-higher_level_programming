#!/usr/bin/python3
"""function module"""


def write_file(filename="", text=""):
    """writes to a txt file"""

    with open(filename, 'w', encoding="utf-8") as f:
        num_chars = f.write(text)
    f.closed
    return num_chars
