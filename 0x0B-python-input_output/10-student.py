#!/usr/bin/python3
"""class module"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialize object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary description of class"""

        if (type(attrs) is list and all(type(x) == str for x in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
