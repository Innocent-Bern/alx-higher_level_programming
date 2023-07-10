#!/usr/bin/python3
"""class module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initializes square"""

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """return string representation of square"""

        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        """returns area of square"""

        return self.__size**2
