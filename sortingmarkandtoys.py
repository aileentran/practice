"""
Hackerrank Interview Prep - Sorting
"""
# Notes
# input: list of prices, int = budget
# output: int - max number of toys mark can buy

# first, sort the prices from least to most
# make a counter

# loop through prices
# if k > 0 and cost < k
# buy it! subtract from k and increase toy counter += 1 

# if cost > k, return counter

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    toys = 0

    for price in prices:
        if price > k:
            return toys

        if price < k:
            k -= price
            toys += 1



#########################################################
# First attempt (long ago~)
# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    budget = k
    bought = 0

    for price in prices:
        budget -= price

        if budget >= 0:
            bought += 1
        else:
            return bought

    return bought