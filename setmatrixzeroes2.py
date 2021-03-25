"""
Leetcode - 73. Set Matrix Zeroes

input: matrix of nums
output: matrix of nums where rows and cols where 0 is at are all 0

note: do not make a new data structure
"""

def setZeroes(matrix):
    return

matrix1 = [
[1,1,1],
[1,0,1],
[1,1,1]
]
# [
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
print(setZeroes(matrix2))
