#!/bin/python3

import sys, collections

def birthdayCakeCandles(n, ar):
    counter = collections.Counter(ar)
    mc = counter.most_common(1)
    return mc[0][1]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
