# input: list of nums - prices as time passes!
# output: num - max profit

def get_max_profit(stock_prices):
	low = stock_prices[0]
	profit = stock_prices[1] - stock_prices[0]

	i = 1

	while i < len(stock_prices):
		curr = stock_prices[i]

		potential = curr - low

		profit = max(potential, profit)

		low = min(curr, low)

		i += 1

	return profit


print(get_max_profit([1, 5, 3, 2])) #4
print(get_max_profit([7, 2, 8, 9])) #7
print(get_max_profit([9, 7, 4, 1])) #-2
print(get_max_profit([1, 1, 1, 1])) #0