#!/usr/bin/python3

"""class that defines a square with size attribute"""


class Square:

    """Class square with private attribute size"""

    def __init__(self, size=0):
        """init square with private attribute size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns area of square"""

        return self.__size * self.__size
