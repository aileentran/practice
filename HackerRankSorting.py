################################################################
"""
input: array of ints
output:
Array is sorted in # swaps
First Element: a[0]
Last Element: a[-1]

Thoughts:
counter for swaps

nested loop?
first loop going through ints in list

inner loop: check currInt against the next nextInt
if bigger x, y = y, x <- unpacking AND swaps += 1

outside all loops
print( the stuff with string interpolation)
nothing to return?

Test Cases:

input: [1, 2, 3]
output:
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

input: [3, 2, 1]
output:
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

"""
# Complete the countSwaps function below.
def countSwaps(a):
	swaps = 0

	for num in a:

		i = 0
		while i < len(a) - 1:

			if a[i] > a[i + 1]:
				a[i], a[i + 1] = a[i + 1], a[i]
				swaps += 1
			i += 1

	print(f'Array is sorted in {swaps} swaps.')
	print(f'First Element: {a[0]}')
	print(f'Last Element: {a[-1]}')

############################################################
"""
input: list of toy prices, k = Mark's budget
output: int - num of toys can buy 

thoughts:
sort the toy prices 
num of toys bought set to 0 
remaining budget

loop through sorted toys
budget -= price 
if budget >= (??) 0:
	num toys += 1
else:
	return num toys bought

TEST CASE
input: 
prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50

output: 4
"""

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