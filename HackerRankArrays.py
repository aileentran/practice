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
	while r <= 3:

		c = 0
		while c <= 3:

			print(f'[r {r}] [c {c}]')

			hourglassSum = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
			print(hourglassSum)

			if greatestSum == None or hourglassSum > greatestSum:
				greatestSum = hourglassSum

			c += 1

		r += 1

	return greatestSum
		