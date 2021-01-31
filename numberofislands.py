"""
Leetcode - Number of Islands

input: grid of 1s and 0s, 1 = land 0 = water
output: num - number of Islands

note
island = surrounded by water and connected by land vertically and horizontally
list of adjacent lands
list of seen
loop through cols until find 1, peek around it.
go through adjacent lands and see if
"""

def numIslands(grid):
    return

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] #1
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] #3

print(numIslands(grid1))
# print(numIslands(grid2))
