#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_mult = []
    for num in my_list:
        if num % 2 == 0:
            list_mult.append("True")
        else:
            list_mult.append("False")
    return (list_mult)
