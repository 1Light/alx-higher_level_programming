#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    for i, j in enumerate(str):
        if i == n:
            continue
        else:
            temp += j
    return temp
