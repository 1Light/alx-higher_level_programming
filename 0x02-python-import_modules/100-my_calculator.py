#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    temp = operators.keys()

    if c not in temp:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        print("{} {} {} {}".format(a, c, b, operators[c](a, b)))
