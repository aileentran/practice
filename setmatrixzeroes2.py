"""
Leetcode - 73. Set Matrix Zeroes

input: matrix of nums
output: matrix of nums where rows and cols where 0 is at are all 0

note: do not make a new data structure

Thoughts
create list of zero tuples
loop through matrix and note where the zeros are

loop through the list of zeroes
unpack where the zeroes already
0 out the row
loop through the col in the row where the zero is and zero those out
"""

def setZeroes(matrix):
    zeroes = []
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col == 0:
                zeroes.append((r, c))

    for zero in zeroes:
        r, c = zero
        matrix[r] = [0] * len(matrix[r]) #set entire row to 0
        for i in range(len(matrix)): # i == row indices in matrix
            matrix[i][c] = 0 #set columns to 0
    
    return matrix

# runtime: O(n^2)
# space complexity: O(n)? bc of zeroes list?

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
