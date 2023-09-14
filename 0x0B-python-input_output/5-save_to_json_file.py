#!/usr/bin/python3

""" A module contains save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """ A function to write json object to a file

    Args:
        my_obj (json): The json object to be written to a file
        filename (txt): The txt file to print the json object in
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
