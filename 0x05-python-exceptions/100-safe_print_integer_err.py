#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    init = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError, Exception):
        print("Exception: ", file=sys.stderr)
        init = False
    return init
