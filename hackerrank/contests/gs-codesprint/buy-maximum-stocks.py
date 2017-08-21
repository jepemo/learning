#!/bin/python3

import sys, math

def reorder_stocks(a):
    values = []
    current_day = 1
    for stock in a:
        values.append((current_day, stock))
        current_day += 1
        
    values = sorted(values, key=lambda x: x[1])
    
    return values
    

def buyMaximumProducts(n, k, a):
    purchased_stocks = 0
    spent = 0.0
    
    stocks_days = reorder_stocks(a)
    
    for sd in stocks_days:
        (current_day, stock_price) = sd
        
        available_amount = k-spent
        allowed_buy = int(available_amount / stock_price)
        stocks_buy = allowed_buy if allowed_buy < current_day else current_day

        purchased_stocks += stocks_buy
        spent += float(stock_price * stocks_buy)

    return purchased_stocks


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)
