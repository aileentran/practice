"""
Leetcode - spiral matrix

input: 2d array of nums
output: list of nums in spiral order; 1st is [0][0] last is the center

Notes:
direction is clockwise: right down left up
are there ever.. two numbers in the center?
will there be repeated numbers inside the matrix? does that even matter..?
we need to "move" the edges that we iterate

empty output array
maybe have an array of seen idxs
"""
def spiralOrder(matrix):
    return

matrix1 = [[1,2,3],[4,5,6],[7,8,9]] #[1,2,3,6,9,8,7,4,5]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] #[1,2,3,4,8,12,11,10,9,5,6,7]

print(spiralOrder(matrix1))
