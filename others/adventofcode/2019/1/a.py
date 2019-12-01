#!/usr/bin/env python3

import sys
import math

test_data = [
[12, 2],
[14, 2],
[1969, 654],
[100756, 33583]
]

def read_input():
    lines = []
    for line in open("input.txt"):
        lines.append(line[:-1])
        
    return lines
    # return open("input.txt").readlines()

def go(i):
    return math.floor(i / 3) - 2

def test():
    for [i, o] in test_data:
        result = go(i)
        print(f"Testing {i}")
        if result != o:
            print(f"!! Expected: {o}, Result: {result}")
            sys.exit(1)  
        
if __name__ == "__main__":
    # test()
    # print(go(
    data = read_input()
    total = 0
    for d in data:
        num = int(d)
        res = go(num)
        total += res
    print(total)