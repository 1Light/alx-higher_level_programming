#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    
    num_args = len(argv) - 1
    count = 0

    for i in range(num_args):
        count += int(argv[i+1])
    print("{}".format(count)) 
