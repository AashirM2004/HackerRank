#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
    # Write your code here
    count = 0
    r = len(prices) - 1
    l = 0
    while l < r:
        if prices[l] + prices[r] <= budget:
            count += r - l # add all combos that use smaller sums than this
            l += 1
        else:
            r -= 1
            
    return count

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)
