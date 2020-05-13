#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    #print(ar)
    del ar[k]
    #print(ar)
    sum_rest = int(sum(ar) / 2)
    #print(sum_rest)
    #print(b)
    
    if sum_rest == b:
        return 'Bon Appetit'
    else:
        return str(b-sum_rest)
    

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
