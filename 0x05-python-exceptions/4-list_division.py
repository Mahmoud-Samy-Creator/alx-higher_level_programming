#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list=[]
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            result_list.append(result)
        except TypeError:
            print("wrong type")
            result_list.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
            continue
        except IndexError:
            result_list.append(0)
            print("out of range")
    return result_list
