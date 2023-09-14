#!/usr/bin/python3
"""
9-student.py
"""


class Student:
    """
    Represents a student with first name, last name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the Student object to a dictionary.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
