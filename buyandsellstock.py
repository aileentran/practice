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
    lowest = prices[0]
    profit = 0

    for price in prices:
        print('price', price)
        if price < lowest:
            lowest = price
            print('lowest', lowest)

        if price - lowest > profit:
            profit = price - lowest

    return profit


# def maxProfit(prices):
#     lowest = prices.copy()
#     lowest.sort()
#     profit = 0
#
#     for l in lowest:
#         purchase_day = prices.index(l)
#         sell = max(prices[purchase_day:])
#         if sell - l > profit:
#             profit = sell - l
#     return profit

prices1 = [7,1,5,3,6,4] #5
prices2 = [7,6,4,3,1] #0
prices3 = [2,4,1] #2

print(maxProfit(prices1))
print(maxProfit(prices2))
print(maxProfit(prices3))
