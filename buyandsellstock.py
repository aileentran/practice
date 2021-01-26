"""
Leetcode - Best Time to Buy and Sell Stock

input: array of prices, idx = day
output: num - max profit

notes:
need to buy stock before selling it
find the index of the lowest price or create a copy of list
have it in ascending order

loop through ascending list
find the index in the list
search from start of lowest price to the rest of the list and find max num
return output = max - cost
"""
def maxProfit(prices):
    lowest = prices.copy()
    lowest.sort()
    profit = 0
    for l in lowest:
        purchase_day = prices.index(l)
        sell = max(prices[purchase_day:])
        profit = sell - l
        return profit
    return profit

prices1 = [7,1,5,3,6,4] #5
prices2 = [7,6,4,3,1] #0

print(maxProfit(prices1))
print(maxProfit(prices2))
