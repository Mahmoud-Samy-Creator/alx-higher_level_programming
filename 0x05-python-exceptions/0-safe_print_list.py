#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    len = 0
    
    for item in my_list:
        len += 1

    try:
        while i < x and i < len:
            print(my_list[i], end="")
            i = i + 1
        print("")
    except:
        print("ERROR")
    
    return (i)


