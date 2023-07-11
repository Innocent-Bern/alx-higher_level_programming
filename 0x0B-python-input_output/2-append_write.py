#!/usr/bin/python3
"""function module"""


def append_write(filename="", text=""):
    """writes to a txt file"""

    with open(filename, 'a', encoding="utf-8") as f:
        num_chars = f.write(text)
    f.closed
    return num_chars
