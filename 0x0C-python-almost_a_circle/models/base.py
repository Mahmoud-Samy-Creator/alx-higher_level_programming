#!/usr/bin/python3

class Base:
    """
    The Base class provides a mechanism for generating unique IDs for objects.

    Attributes:
        __nb_objects (int): A private class variable to keep track of the number of instances created.
        id (int): An instance variable representing the unique ID of an object.

    Methods:
        __init__(self, id=None): Initializes a Base object. If an ID is provided, it uses that ID; 
        otherwise, it auto-generates a unique ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): An optional ID to assign to the object. If not provided, a unique ID will be generated.

        Note:
            If an ID is provided, it will be used. If no ID is provided, a unique ID will be assigned, 
            starting from 1 and incrementing for each new object created.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
