#!/bin/python3

import sys, math

def solve(n, p):
    front = int(p / 2)
    back = n - (int(p/2)+math.ceil(n/2))
    
    return min(front, back)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
