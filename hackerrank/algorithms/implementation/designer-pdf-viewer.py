#!/bin/python3

import sys


h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num = 0
for w in word:
    ind = 0
    for a in alphabet:
        if a == w:
            pos = ind
            break
        ind = ind + 1
        
    height = h[ind]
    if height > num:
        num = height
        
print(len(word) * num)
