#!/bin/python3

import sys
from collections import Counter

def migratoryBirds(n, ar):
    counter = Counter(ar)
    most_common = counter.most_common(1)
    most_common = sorted(most_common, key=lambda t: t[0])
    return most_common[0][0]
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
