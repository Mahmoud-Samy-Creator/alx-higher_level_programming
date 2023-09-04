#!/usr/bin/python3
"""Defines a function adds 2 integers
Attributes:
    add_integer: function that adds two integers
"""


def add_integer(a, b=98):
    """Add 2 integers or float values

    Args:
        a (int): 1st argument
        b (int, optional): 2nd argument. Defaults to 98.

    Raises:
        TypeError: if a or b are not int or float

    Returns:
        int: a + b
    """
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be integer")

    if not isinstance(b, int):
        raise TypeError("b must be integer")
    return a + b
