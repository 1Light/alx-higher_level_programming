#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer we want to print

    Returns:
        False - For TypeError or ValueError
        True - Otherwise
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
