"""
Leetcode - 1337. The K Weakest Rows in a Matrix

input: 2d matrix of nums, 1 = soldiers, 0 = civilians AND k = num of weakest rows
output: array of nums - idx of weakest rows
(length about half of input rounded up)?

Notes: soldiers are always first
create a dictionary of indices as keys and counter of soldiers as values
or an array w/ idx = row and value = keys
"""

def kWeakestRows(mat, k):
    return


mat1 =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k1 = 3
#[2,0,3]

mat2 =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k2 = 2
#[0,2]

print(kWeakestRows(mat1, k1))
print(kWeakestRows(mat2, k2))
