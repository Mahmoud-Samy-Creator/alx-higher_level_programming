#!/usr/bin/python3

""" A module contains write_file method
"""


def write_file(filename="", text=""):
    """ A function to write on a file
    Args:
        write_file(str, STR): file_name to write on & the str written
    """
    with open(filename, "w") as file:
        no_of_chars = file.write(text)
        return no_of_chars
