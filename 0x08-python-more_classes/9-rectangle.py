#!/usr/bin/python3
"""class module"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize obj"""

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """prints char # to represent rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rtn = []
        for i in range(self.__height):
            for x in range(self.__width):
                rtn.append("#")
            rtn.append("\n")
        return "".join(rtn)

    def __repr__(self):
        """rtns string representation of rectangle"""

        return f"Rectangle ({self.__width}, {self.__height})"

    def __del__(self):
        """prints msg on deletion"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """rtn rectangle with bigger area"""

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """rtns a square"""

        return cls(size, size)
