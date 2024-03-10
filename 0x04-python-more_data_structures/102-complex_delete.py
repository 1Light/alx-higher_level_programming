#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    my_list = list(a_dictionary.items())

    my_list = [x for x in my_list if x[1] != value]

    my_dict = dict(my_list)
    
    a_dictionary.clear()
    a_dictionary.update(my_dict)
    
    return a_dictionary
