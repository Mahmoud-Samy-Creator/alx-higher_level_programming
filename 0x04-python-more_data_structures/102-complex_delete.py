#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for item, val in a_dictionary.items():
            if val == value:
                del a_dictionary[item]
                break
    return a_dictionary
