#!/bin/python3

import sys


sentence = input().strip()
num_words = 1
for letter in sentence:
    if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
        num_words = num_words+1
        
print(num_words)
