#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    len = 0
    for item in my_list:
        len += 1

    while i < x and i < len:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            print("IndexError: list index out of range")
            break
    print("")
    return (i)
