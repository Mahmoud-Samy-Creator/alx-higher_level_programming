#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    if idx < 0 or idx >= len(my_list):
        list_copy = my_list.copy()
        return list_copy
    list_2 = my_list.copy()
    list_2[idx] = element
    return list_2
