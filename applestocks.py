# def get_max_profit(stock_prices):

#     # Calculate the max profit
#     low = stock_prices[0]
#     low_i = 0

#     high = stock_prices[1]
#     high_i = 1

#     profit = high - low

#     i = 1

#     while i < len(stock_prices):
#         stock = stock_prices[i]
#         print('stock', stock)


#         if stock < low and i != low_i:
#             low = stock
#             low_i = i

#         elif stock > high and i > low_i and i != high_i:
#             high = stock
#             high_i = i

#         possible = high - low

#         if possible > profit:
#             profit = possible

#         print('low', low)
#         print('low_i', low_i)

#         print('high', high)
#         print('high_i', high_i)

#         print('profit', profit)

#         print('\n\n\n')
    	
#         i += 1

#     # print('low', low)
#     # print('high', high)

#     return profit




def get_max_profit(stock_prices):

    # Calculate the max profit
    low = stock_prices[0]
    profit = stock_prices[1] - stock_prices[0]

    i = 1

    while i < len(stock_prices):
        print('low', low)
        print('profit', profit)
        curr = stock_prices[i]
        print('curr', curr)
        potential = curr - low
        print('potential', potential)
        profit = max(potential, profit)
        print('profit', profit)
        low = min(curr, low)
        print('low', low)
        print('\n\n')

        i += 1

    return profit


# print(get_max_profit([1, 5, 3, 2])) #4
print(get_max_profit([7, 2, 8, 9])) #7
# print(get_max_profit([9, 7, 4, 1])) #-2
# print(get_max_profit([1, 1, 1, 1])) #0