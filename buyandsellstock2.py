"""
Leetcode - 121. Best Time to Buy and Sell Stock

input: list of nums - i : day, list[i] : price
output: num - greatest amount of profit

Notes:
can only sell after you buy stock

Brute force solution:
empty profit variable
loop through the numbers
slice and look at the days following to get maximum number
if curr num - max num > profit
then set the profit variable to the new difference
outside of the loop, return profit

Two pointer solution:
have empty profit variable
initialize left (buy) to 0 and right(sell) to i
loop through idxs
if right price is < left price
scoot the left pointer and right pointer over
else subtract right price from left price
if > profit, then set profit = right - left prices
outside loop, return profit

Leetcode solution
empty profit variable
set minimum number to infinity

loop through list
if the price is < minimum, minimum = price
else price - minimum > profit, profit = that difference

return profit
"""
def maxProfit(prices):
    profit = 0
    minimum = float('inf')

    for price in prices:
        if price < minimum:
            minimum = price
        elif price - minimum > profit:
            profit = price - minimum

    return profit

prices1 = [7,1,5,3,6,4] #5 = 6 (day 5) - 1 (day 2)
prices2 = [7,6,4,3,1] #0 - no transactions

print(maxProfit(prices1))
print(maxProfit(prices2))
