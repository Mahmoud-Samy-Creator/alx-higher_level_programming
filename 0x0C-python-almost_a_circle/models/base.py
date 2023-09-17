#!/usr/bin/python3

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
