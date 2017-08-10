#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
"""
a.sort()
b.sort()

factors = []

for i in range(2, max([max(a), max(b)])):
    c = True
    for an in a:
        if i % an != 0:
            c = False
            break
          
    if c:    
        for bn in b:
            if bn % i != 0:
                c = False
                break
                
    if c and i not in factors:
        factors.append(i)
                
print(len(factors))
"""

a.sort()
b.sort()
A = 0
for i in range(a[-1],(b[0]+1)):
    y = 0
    x = 0
    for j in range(n):
        if(i%a[j] == 0):
            y = y + 1
        else:
            break
    if(y == n):
        for k in range(m):
            if(b[k]%i == 0):
                x= x+1
            else:
                break

        if(x == m):
            A = A + 1    

print(A)
