#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = []

    for x in matrix:
        new_row = []

        for i in x:
            new_row.append(i ** 2)

        new_matrix.append(new_row)

    return new_matrix
