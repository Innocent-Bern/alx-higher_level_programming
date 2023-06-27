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

        self.size = size

    def area(self):
        """Returns area of square"""

        return self.__size * self.__size

    @property
    def size(self):
        """Getter method to retrieve size attr"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size attr"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Print square with # character"""

        if self.size == 0:
            print()
            return None

        for i in range(self.size):
            for x in range(self.size):
                print("#", end="")
            print()
