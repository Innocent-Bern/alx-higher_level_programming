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

        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height attr"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attr"""

        if not isinstance(self.__height, int):
            raise TypeError("width must be an integer")
        if self.__height < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
