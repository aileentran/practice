"""
Leetcode - 200. Number of Islands

input: grid of 1s and 0s, 1 = land 0 = water
output: num - number of Islands

Note
island = surrounded by water and connected by land vertically and horizontally
list of adjacent lands
list of seen
loop through cols until find 1, peek around it (up, down, left, right).
go through adjacent lands and see if

Approach: using depth-first-search whenever encountering land
marking seen in the grid
either make copy of grid or adjust directly to save space
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
