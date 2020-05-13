#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
    
sorted_t = sorted(unsorted, key=lambda x: int(x))
for s in sorted_t:
    print(s)
