#!/usr/bin/python3

""" Module contains append_write method
"""


def append_write(filename="", text=""):
    """ A function that appends a string at the end of a text file
    Args:
        append_write(str, str): The file opened, the data appended
    """
    with open(filename, "a", encoding="UTF-8") as file:
        no_of_chars = file.write(text)
        return no_of_chars
