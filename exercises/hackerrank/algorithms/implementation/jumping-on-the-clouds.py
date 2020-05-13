#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    it = 0
    num_steps = 0
    input_size = len(c)
    while it < input_size:
        if it >= input_size-1:
            break

        #print(f"c[{it+2}]={c[it+2]}")
        if it+2 >= input_size or c[it+2] == 1:
            it += 1
            num_steps += 1
        else:
            it += 2
            num_steps += 1

        print("it=", it)

    return num_steps 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
