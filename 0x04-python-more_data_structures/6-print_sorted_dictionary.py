#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = sorted(a_dictionary.keys())
    for item in result:
        print("{}: {}".format(item, a_dictionary[item]))
