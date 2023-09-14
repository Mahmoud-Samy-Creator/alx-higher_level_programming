#!/usr/bin/python3

""" A module contains load_from_json_file
"""

import json


def load_from_json_file(filename):
    """ A function to write json object to a file

    Args:
        filename (json): The file to be deserialized
    """
    with open(filename, "r") as file:
        return (json.load(file))
