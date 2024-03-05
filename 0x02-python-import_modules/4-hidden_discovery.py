#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    
    name = dir(hidden_4)
    
    for i in range(len(name)):
        if not name[i].startswith("__"):
            print(name)
