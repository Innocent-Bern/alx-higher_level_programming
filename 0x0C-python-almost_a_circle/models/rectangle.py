#!/usr/bin/python3
"""class module"""

Base = __import__('base').Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes object"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints out the rectangle"""

        [print() for y in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """override str method"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, 
                self.__x, 
                self.__y, 
                self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        count = 0
        for x in args:
            if count == 0:
                self.id = x
            if count == 1:
                self.__width = x
            if count == 2:
                self.__height = x
            if count == 3:
                self.__x = x
            if count == 4:
                self.__y = x
            count += 1

        if len(args) == 0:
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k == "id":
                        self.id = v
                    if k == "width":
                        self.__width = v
                    if k == "height":
                        self.__height = v
                    if k == "x":
                        self.__x = v
                    if k == "y":
                        self.__y = v

    def to_dictionary(self):
        """return dictionary rep of rectangle"""

        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
