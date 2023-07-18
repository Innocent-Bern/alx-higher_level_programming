#!/usr/bin/python3
"""class module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes object"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""

        return self.__width

    @size.setter
    def size(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """override str method"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        count = 0
        for x in args:
            if count == 0:
                self.id = x
            if count == 1:
                self.width = x
                self.height = x
            if count == 2:
                self.x = x
            if count == 3:
                self.y = x
            count += 1

        if len(args) == 0:
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k == "id":
                        self.id = v
                    if k == "size":
                        self.width = v
                        self.height = v
                    if k == "x":
                        self.x = v
                    if k == "y":
                        self.y = v

    def to_dictionary(self):
        """return dictionary rep of rectangle"""

        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
