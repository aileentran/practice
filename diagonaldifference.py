"""
HackerRank - Diagonal Difference

input: square matrix
output: num - absolute difference between both diagonals

diagonals in a matrix => [same num, same num] in ascending and descending
"""
def diagonalDifference(arr):
    
    return

a1 = [
[1, 2, 3]
[4, 5, 6]
[9, 8, 9]
]

a2 = [
[11, 2, 4]
[4, 5, 6]
[10, 8, -12]
]
print(diagonalDifference(a1)) #2 - diagonals [1, 5, 9], [3, 5, 9]
print(diagonalDifference(a2)) #15 - diagonals [11, 5, -12], [4, 5, 10]
