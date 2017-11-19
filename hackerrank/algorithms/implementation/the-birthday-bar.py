#!/bin/python3

import sys, itertools

def grouper(n, iterable):
    if (len(iterable)) < n:
        return []
    elif len(iterable) == n:
        return [list(iterable)]
    else:
        a = []
        a.append(iterable[:n])
        a.extend(grouper(n, iterable[1:]))
        return a
        #return [l for l in [list(e) for e in zip([iterable[:n], grouper(n, iterable[1:])])]]
        #return [iterable[:n], grouper(n, iterable[1:])]
        #return [iterable[:n], [list(e) for e in zip(grouper(n, iterable[1:]))]]

def solve(n, s, d, m):
    groups = list(grouper(m, s))
    #print(groups)
    return len(list(filter(lambda g: sum(g) == d, groups)))

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
