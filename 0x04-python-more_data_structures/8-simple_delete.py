#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):

    new_dictionary = {}

    for x in a_dictionary:
        if x == key:
            continue

        else:
            new_dictionary[x] = a_dictionary[x]

    a_dictionary.clear()
    a_dictionary.update(new_dictionary)

    return a_dictionary
