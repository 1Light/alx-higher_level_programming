#!/usr/bin/python3


def weight_average(my_list=[]):

    if my_list == []:
        return 0

    total_score = 0
    total_weight = 0

    for x, y in my_list:
        total_score += x * y
        total_weight += y

    result = total_score / total_weight

    return result
