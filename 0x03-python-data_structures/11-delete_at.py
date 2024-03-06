#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if idx < 0 or idx >= len(my_list):
        return my_list
    
    new_list = []
    for x in my_list:
        if x == my_list(idx):
            continue
        else:
            new_list += [x]
    return new_list
