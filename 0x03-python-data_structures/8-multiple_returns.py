#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    if sentence == "":
        char = None
    else:
        char = sentence[0]

    my_tuple = (length, char)
    return my_tuple
