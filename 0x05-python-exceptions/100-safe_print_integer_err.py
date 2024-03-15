#!/usr/bin/python3

import sys


def safe_print_integer_err(value):

    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True

        else:
            raise TypeError

    except TypeError:
        sys.stderr.write(
                "Exception: Unknown format code 'd' for object of type 'str'\n"
                )
        return False
