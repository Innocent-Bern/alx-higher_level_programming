#!/usr/bin/python3
"""module that checks for subclass"""


def inherits_from(obj, a_class):
    """checks if obj is instance of a_class"""

    return isinstance(obj, a_class.__bases__)
