#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if isinstance(my_list, list):
        num = len(my_list) - 1
        for i in range(num, -1, -1):
            print("{:d}".format(my_list[i]))
