"""
Leetcode - 121. Best Time to Buy and Sell Stock

input: list of nums - i : day, list[i] : price
output: num - greatest amount of profit

Notes:
can only sell after you buy stock

Thoughts
empty profit variable

loop through the numbers
slice and look at the days following to get maximum number
if curr num - max num > profit
then set the profit variable to the new difference

outside of the loop, return profit
"""
def maxProfit(prices):
    profit = 0

    for p in range(len(prices) - 1):
        buy = prices[p]
        max_sell = max(prices[p + 1:])

        if max_sell > buy and (max_sell - buy) > profit:
            profit = max_sell - buy

    return profit

prices1 = [7,1,5,3,6,4] #5 = 6 (day 5) - 1 (day 2)
prices2 = [7,6,4,3,1] #0 - no transactions

print(maxProfit(prices1))
print(maxProfit(prices2))
