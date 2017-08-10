#!/bin/python3

import sys

def getRecord(s):
    nmax = 0
    nmin = 0
    max_record = s[0]
    min_record = s[0]
    
    for p in s:
        if p > max_record:
            max_record = p
            nmax = nmax + 1
            
        if p < min_record:
            min_record = p
            nmin = nmin + 1
    
    return [nmax, nmin]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
