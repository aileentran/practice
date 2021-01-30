"""
Leetcode - 73. Set Matrix Zeroes

input: matrix of nums
output: None, set the value in place

notes: set row and cols w/0 to 0
"""
def setZeroes(matrix):
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
print(setZeroes(matrix1))
