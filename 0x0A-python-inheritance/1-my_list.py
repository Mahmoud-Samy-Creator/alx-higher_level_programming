#!/usr/bin/python3

"""
===========================
Module of class inheritance
===========================
"""


class list:
    def __init__(self):
        self.new_list = []


class MyList(list):
    def __str__(self):
        return f"{self.new_list}"

    def append(self, obj):
        self.new_list.append(obj)

    def print_sorted(self):
        sorted_list = sorted(self.new_list)
        print(sorted_list)
