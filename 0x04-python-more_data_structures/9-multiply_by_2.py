#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = a_dictionary.copy()
    for key in result:
        result[key] *= 2
    return result
