#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    init = True
    try:
        
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: ", e, file=stderr)
        init = False
    return init
