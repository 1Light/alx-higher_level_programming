#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list == []:
        return None

    x = 0

    for i in range(len(my_list)):
        if x < my_list[i]:
            x = my_list[i]
        else:
            continue
    return x
