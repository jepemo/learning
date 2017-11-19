#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

v = sorted([a, b, c, d, e])

print(sum(v[0:4]), sum(v[1:]))
