#!/usr/bin/env python3

import math

def read_input():
    lines = []
    for line in open("input.txt"):
        lines.append(int(line[:-1]))
        
    return lines
    
def calc(i):
    return math.floor(i / 3) - 2

if __name__ == "__main__":
    data = read_input()
    total = 0
    for d in data:
        res = calc(d)
        total += res
        while res > 0:
            res = calc(res)
            if res > 0:
                total += res
        
    print(total)