#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice_result = 0
bob_result = 0
alice_points = [a0, a1, a2]
bob_points = [b0, b1, b2]

for i in range(0, len(alice_points)):
    ap = alice_points[i]
    bp = bob_points[i]
    if (ap > bp):
        alice_result = alice_result + 1
    elif (bp > ap):
        bob_result = bob_result + 1
    else:
        pass
    
print (alice_result, bob_result)
