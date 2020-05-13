#!/bin/python3

import sys

def available(i, j):
    return i <= 3 and j <= 3

def sum_hourglass(matrix, i, j):
    return matrix[i][j] + \
           matrix[i][j+1] + \
           matrix[i][j+2] + \
           matrix[i+1][j+1] + \
           matrix[i+2][j] + \
           matrix[i+2][j+1] + \
           matrix[i+2][j+2]
            
            

def calculate_sum(matrix):
    maximum = None
    for row_ind in range(0, len(matrix)):
        row = matrix[row_ind]
        for col_ind in range(0, len(row)):
            if available(row_ind, col_ind):
                result = sum_hourglass(matrix, row_ind, col_ind)
                if maximum == None or maximum < result:
                    maximum = result
            
    return maximum

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
print(calculate_sum(arr))
