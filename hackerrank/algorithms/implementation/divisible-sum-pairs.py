#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    numPairs = 0
    
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            ai = ar[i]
            aj = ar[j]
            
            if (ai+aj) % k == 0:
                numPairs = numPairs + 1
    
    return numPairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
