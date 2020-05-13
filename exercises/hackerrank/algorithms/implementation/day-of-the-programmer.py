#!/bin/python3

import sys

def solve(year):
    result = ''
    
    leap_year = False
    add_days = 0
    month='09'
    if year < 1918:
        leap_year = year % 4 == 0
    elif year == 1918:
        leap_year = (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)
        add_days = 13
        #month='08'
    else:
        leap_year = (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)
        
    num_leap = 29 if leap_year else 28
    
    ndays = 31+num_leap+31+30+31+30+31+31
    res_day = 256-ndays+add_days
    #print(res_day)
    
    #if res_day < 0:
    #    res_day = 31+res_day
    
    result = str(res_day) + "." + month + "." + str(year)
    
    return result

year = int(input().strip())
result = solve(year)
print(result)
