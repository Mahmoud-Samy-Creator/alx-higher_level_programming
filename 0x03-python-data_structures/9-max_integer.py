#!/usr/bin/python3
def max_integer(my_list=[]):
    max = -5
    if my_list is None or my_list == []:
        return None
    for int in my_list:
        if int > max:
            max = int
    return (max)
