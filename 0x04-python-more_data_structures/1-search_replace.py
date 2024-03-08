#!/usr/bin/python3


def search_replace(my_list, search, replace):

    copy_list = my_list[:]
    new_list = []

    for i in range(len(copy_list)):
        if copy_list[i] == search:
            copy_list[i] = replace

        new_list.append(copy_list[i])

    return new_list
