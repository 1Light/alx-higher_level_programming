#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    A message is printed if a ValueError occurs 
    Args:
        value (int): The integer to output.

    Returns:
        False - For a TypeError or ValueError occurs
        True - Otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
