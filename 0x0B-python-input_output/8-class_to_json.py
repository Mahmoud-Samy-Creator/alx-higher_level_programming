#!/usr/bin/python3

""" A module contains class_to_json function
"""


def class_to_json(obj):
    """
    A function saves a dictionary description
    of a class object to a json file
    """
    dict = vars(obj)
    return dict
