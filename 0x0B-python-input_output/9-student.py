#!/usr/bin/python3
"""class module"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialize object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary description of class"""

        return self.__dict__
