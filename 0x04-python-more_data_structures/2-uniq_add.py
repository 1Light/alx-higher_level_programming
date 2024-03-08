#!/usr/bin/python3


def uniq_add(my_list=[]):

    unique_integers = set()

    for num in my_list:
        unique_integers.add(num)

    sum = 0

    for x in unique_integers:
        sum += x

    return sum
