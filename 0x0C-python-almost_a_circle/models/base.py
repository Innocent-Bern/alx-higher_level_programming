#!/usr/bin/python3
"""class module"""


import json
import os.path


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize object"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns json rep of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """returns a list of json string representation"""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes list_objs to a file"""

        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_arr = [a.to_dictionary() for a in list_objs]
                f.write(Base.to_json_string(dict_arr))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""

        if cls.__name__ == "Rectangle":
            return cls(1, 1).update(**dictionary)
        return cls(1).update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        f_name = str(cls.__name__) + ".json"
        if os.path.isfile(f"./{f_name}"):
            with open(f_name, "r") as f:
                return [cls.create(**d) for d in Base.from_json_string(f.read())]
        return []


