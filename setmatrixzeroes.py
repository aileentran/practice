"""
Leetcode - 73. Set Matrix Zeroes

input: matrix of nums
output: None, set the value in place

notes: set row and cols w/0 to 0
"""
def setZeroes(matrix):
    # make a note of where the 0 is
    zeroes = [] #idx of where the zero is in matrix!
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col == 0:
                zeroes.append((r, c))

    for zero in zeroes:
        r, c = zero
        matrix[r] = [0] * len(matrix[0])
        for r, row in enumerate(matrix):
            matrix[r][c] = 0
    return

matrix1 = [
[1,1,1],
[1,0,1],
[1,1,1]
]
#[
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]

matrix2 = [
[0,1,2,0],
[3,4,5,2],
[1,3,1,5]
]
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# print(setZeroes(matrix1))
setZeroes(matrix2)
