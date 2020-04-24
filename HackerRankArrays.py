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
input: q -> array of ints (people's position in line)
output: PRINT int (min swaps necessary) OR "Too chaotic" 

swap = bribe - behind moves in front
people can move up max 2 places 

thoughts
1. using a range of ordered stuff to compare current q to 
2. ordered = idx + 1 
3. like bubble sorting -> look at left person and if person is greater, keep swappin

peeps behind an move up max 2 idxs. problem is.. front person can be continually bribed by new people behind them..? /)_(\

make swap counter
make places moved counter = {num : #places moved}

nested loop: outer = overall order, inner = move until it's in the right place 

outer loop
for each num
counter[num] = 0??

inner loop: while?? 
until num == idx + 1
if counter[num] > 2: print "Too Chaotic"
num, num @ idx + 1 = num @ idx + 1, num
swap += 1
counter[num] += 1 

idx += 1

out of all loops
print swaps?

TEST CASE

Input: line = [2, 1, 5, 3, 4]
Output: 3

Input: line = [2, 5, 1, 3, 4]
Output: "Too chaotic"
"""

#####################################################


		