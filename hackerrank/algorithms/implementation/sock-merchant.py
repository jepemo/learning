#!/bin/python3

import sys, math
from collections import Counter

def sockMerchant(n, ar):
    numSocks = 0
    counter = Counter(ar)
    for key in counter.keys():
        #print(counter[key], '->', math.floor(counter[key] / 2))
        numSocks = numSocks + math.floor(counter[key] / 2)
        
    return numSocks

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
