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
# Complete the hourglassSum function below.
def hourglassSum(arr):
