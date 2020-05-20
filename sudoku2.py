"""
Practicing sudoku prob again!
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

def sudoku(grid):

	# checking rows
	for row in grid:
		num_count = {}
		for num in row:
			if num in num_count:
				return False
			else:
				num_count[num] = 1

	# checking columns
	nrow = len(grid)
	ncol = len(grid[0])

	col = 0

	while col < ncol:
		num_count = {}
		row = 0
		
		while row < nrow:
			num = grid[row][col]
			if num in num_count:
				return False
			else:
				num_count[num] = 1

			row += 1

		col += 1 

	# check 3x3
	"""
	origin starting point thingies!
	origin1 = (0,0)
	origin2 = (0, 3)
	origin3 = (0, 6)
	(0, 0), (0, 3), (0, 6)
	(3, 0), (3, 3), (3, 6)
	(6, 0), (6, 3), (6, 6)

	"""
	origins = []

	row = 0

	while row <= 6:
		col = 0

		while col <= 6:
			origins.append((row, col))
			col += 3

		row += 3

	


	return True


print(sudoku(good)) #True
print(sudoku(bad))	#False