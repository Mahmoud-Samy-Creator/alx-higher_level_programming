#!/usr/bin/python3


""" A module contains to_json_string method
"""


import json


def to_json_string(my_obj):
    """A function returns json representation of an object
    Args:
        object: The object to be serialized
    Return:
        JSON representation
    """
    return json.dumps(my_obj)
