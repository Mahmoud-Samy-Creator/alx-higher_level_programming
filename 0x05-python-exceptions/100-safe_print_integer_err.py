#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    init = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: ", e, file=stderr)
        init = False
    return init
