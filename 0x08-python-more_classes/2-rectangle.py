#!/usr/bin/python3
"""class module"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize obj"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width attr"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attr"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height attr"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attr"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """return area of rectangle"""

        return (2 * self.__width) + (2 * self.__height)
