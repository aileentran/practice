"""
Write a function valid_sudoku() that returns
True => if the passed in solution is valid
False => if the passed in solution is invalid	

solution = row, col, and 3 x 3 boxes have nums 1-9 w/out repeats

3x3:
-starts at [row][col]
-upper left: [row][col + 3]
-lower left: [row + 3][col + 3]
-lower right: [row + 3][col]
*need to make sure never out of bounds! 

thoughts
make a set for 1-9? 
dictionary w/ counter? hmm.. item[key]: counter[val]
check each row, col, and.. 3x3 against it -> if counter > 1 = return false 

outside, return true! 
"""

good = [
 [8,3,5,4,1,6,9,2,7],
 [2,9,6,8,5,7,4,3,1],
 [4,1,7,2,9,3,6,5,8],
 [5,6,9,1,3,4,7,8,2],
 [1,2,3,6,7,8,5,4,9],
 [7,4,8,5,2,9,1,6,3],
 [6,5,2,7,8,1,3,9,4],
 [9,8,1,3,4,5,2,7,6],
 [3,7,4,9,6,2,8,1,5]
]

bad = [
 [8,3,5,4,1,6,9,2,7],
 [2,9,6,8,5,7,4,3,1],
 [4,1,7,2,9,3,6,5,8],
 [5,6,9,1,3,4,7,8,2],
 [1,2,3,6,7,8,5,4,9],
 [7,4,8,5,2,9,1,6,3],
 [6,5,2,7,8,1,3,9,4],
 [9,8,1,3,4,5,2,7,6],
 [3,7,4,9,6,2,8,1,1]
]

def valid_sudoku(solution):
	# code goes here
	num_count = {}
	nrow = len(solution)
	ncol = len(solution[0])

	# check rows (horizontal)
	for row in solution:
		for col in row:
			if col in num_count:
				return False
			else:
				num_count[col] = 1
		# resetting the count
		num_count = {}

	# check columns (vertical)
	# entire columns are.. [row + 1][col]
	i = 0

	while i < ncol:
		k = 0
		while k < nrow:
			num = solution[k][i]

			if num in num_count:
				return False
			else:
				num_count[num] = 1

			k += 1

		num_count = {}

		i += 1


	return True

print(valid_sudoku(good)) # True
print(valid_sudoku(bad)) # False
