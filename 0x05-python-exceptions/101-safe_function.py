#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: A function
        args: Arguments of the function fct.

    Returns:
        None - For an error.
        The result of the call to the fct - Otherwise
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
