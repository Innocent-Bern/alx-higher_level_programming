#!/usr/bin/python3
"""module that checks for subclass"""


def inherits_from(obj, a_class):
    """checks if obj is instance of a_class"""

    for i in type(obj).__bases__: 
        if i is a_class or type(obj) == a_class:
            return True
    return False
