#!/usr/bin/python3

def add_integer(a, b=98):
    '''A function to add 2 numbers'''
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be integer")

    if not isinstance(b, int):
        raise TypeError("b must be integer")
    return a + b
