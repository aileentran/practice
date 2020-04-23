# thoughts
# input: 2d array
# output: int = greatest sum of hour glass
# note! try to keep in bounds: row and col idx <= 3

# make empty sum variable = null (bc.. don't know what sum might be) 
# use while loop with row = 0, col = 0 until both <= 3 (???)
# make hourglass sum variable = null
# sum [row][col], [row][col + 1], [row][col + 1], 
# [row + 1][col + 1], 
# [row + 2][col], [row + 2][col + 1], [row + 2][col + 2]
# if sum == null or hourglass sum > sum
# sum = hourglass sum

# return sum
"""
test case

input:
arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

output: 19
"""

# Complete the hourglassSum function below.
def hourglassSum(arr):

	greatestSum = None

	r = 0
	while r <= len(arr) - 3:

		c = 0
		while c <= len(arr) - 3:

			print(f'[r {r}] [c {c}]')

			hourglassSum = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
			print(hourglassSum)

			if greatestSum == None or hourglassSum > greatestSum:
				greatestSum = hourglassSum

			c += 1

		r += 1

	return greatestSum

"""
test case

input:
arr = [1, 2, 3, 4, 5]
d = 4

output: [5, 1, 2, 3, 4]

"""

def rotLeft(a, d):

	i = 0

	while i < d:
		end = a.pop(0)
		a.append(end)

		i += 1

	return a

"""
thoughts:
input: q = array of ints
output: int = # of swaps OR "Too chaotic"

create ordered list to compare q to 
ordered = list(range(1, len(q) + 1)) * range exclusive! 
set swaps to "Too chaotic"

use while loop => two pointers: one at ordered list and one at q
subtract q from ordered item
if difference is not in range(-2, 3) -> return "too chaotic"
else: if swaps == "Too chaotic", swaps = 1
else: swaps += 1

outside loop
return swaps // 2 => bc.. prob overlapping counts?? 


TEST CASE

Input: line = [2, 1, 5, 3, 4]
Output: 3

Input: line = [2, 5, 1, 3, 4]
Output: "Too chaotic"
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
	# ordered = list(range(1, len(q) + 1))
	swaps = "Too chaotic"

	print('ordered', ordered)

	i = 0

	while i < len(q):
		# order = ordered[i]
		# bribed = q[i]
		# places = order - bribed
		# print(places)


		i += 1

	return swaps

		