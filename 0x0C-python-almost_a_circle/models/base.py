#!/usr/bin/python3

import json

class Base:
    """
    Provides unique ID generation for objects.

    Attributes:
        __nb_objects (int): Tracks the number of instances created.
        id (int): Represents the object's unique ID.

    Methods:
        __init__(self, id=None): Initializes a Base object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): ID to assign.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None or list_objs == []:
                jsonfile.write("[]")
            else:
                list_of_dictionaries = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_of_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)