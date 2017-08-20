#!/bin/python3

import sys, math

def buyMaximumProducts(n, k, a):
    purchased_stocks = 0
    current_day = 1
    spent = 0.0
    for stock_price in a:
        available_amount = k-spent
        allowed_buy = int(available_amount / stock_price)
        stocks_buy = allowed_buy if allowed_buy < current_day else current_day

        purchased_stocks += stocks_buy
        spent += float(stock_price * stocks_buy)

        current_day += 1

    return purchased_stocks


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)
