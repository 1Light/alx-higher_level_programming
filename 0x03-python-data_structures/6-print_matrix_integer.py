#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    if not matrix:
        return None
    for submatrix in matrix:
        if len(submatrix) == 0;
            print()
        for i in range(len(submatrix):
                print("{:d}".format(submatrix[i]),
                    end="\n" if i is len(submatrix) -1 else " ")
