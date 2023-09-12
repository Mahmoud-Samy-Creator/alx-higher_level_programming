#!/usr/bin/python3
import json

""" A module contains to_json_string method
"""


def to_json_string(my_obj):
    """A function returns json representation of an object
    Args:
        object: The object to be serialized
    """
    return (json.dumps(my_obj))
