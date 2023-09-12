#!/usr/bin/python3


""" A module contains from_json_string method
"""


import json


def from_json_string(my_str):
    """A function returns an obect from json representation
    Args:
        object: The object to be serialized
    Return:
        string representation
    """
    return json.loads(my_str)
