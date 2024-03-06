#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    a1, a2 = tuple_a[:2]

    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    b1, b2 = tuple_b[:2]

    c1 = a1 + b1
    c2 = a2 + b2

    tuple_c = (c1, c2)
    return tuple_c
