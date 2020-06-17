def get_max_profit(stock_prices):

    # Calculate the max profit
    low = stock_prices[0]
    low_i = 0

    high = stock_prices[1]
    high_i = 1

    profit = high - low

    i = 0

    while i < len(stock_prices):
    	stock = stock_prices[i]
    	

    	if stock < low:
    		low = stock
    		low_i = i

    	elif stock > high and i > low_i:
    		high = stock
    		high_i = i

    	possible = high - low

    	if possible > profit:
    		profit = possible

    	
    	i += 1

    print('low', low)
    print('high', high)

    return profit






print(get_max_profit([1, 5, 3, 2])) #4
print(get_max_profit([7, 2, 8, 9])) #7
print(get_max_profit([9, 7, 4, 1])) #-2
print(get_max_profit([1, 1, 1, 1])) #0