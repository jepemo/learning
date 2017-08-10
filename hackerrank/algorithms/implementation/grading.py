#!/bin/python3

import sys, math

def solve(grades):
    result = []
    for g in grades:
        if g < 38:
            result.append(g)
        else:
            next_mult = 5 * math.ceil(g/5)
            if (next_mult-g) < 3:
                result.append(next_mult)
            else:
                result.append(g)
                
    return result

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
