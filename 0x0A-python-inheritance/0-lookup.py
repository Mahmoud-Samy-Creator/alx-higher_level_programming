#!/usr/bin/python3

"""
========================
A file for lookip module
========================
"""
def lookup(obj):
    """Returns a list of available attributes and methods"""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
