#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

#rotate array
#for t in range(k):
#    a = [a[-1]] + a[0:-1]

for a0 in range(q):
    m = int(input().strip())
    pos = (m - k) % n
    print(a[pos])
