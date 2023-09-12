#!/usr/bin/python3

""" Module contain read_file method
"""


def read_file(filename=""):
    """ A function that reads a file content
    Args:
        filename (str, optional): The name of the file to read
    """
    with open(filename, "r", encoding="UTF-8") as file:
        read_data = file.read()
        print(read_data, end="")
