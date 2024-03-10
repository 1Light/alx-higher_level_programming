#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return None

    value_list = [value for value in a_dictionary.values()]

    max_value = value_list[0]

    for i in range(len(value_list)):
        if value_list[i] > value_list[0]:
            max_value = value_list[i]

    for key, value in a_dictionary.items():
        if value == max_value:
            return key
