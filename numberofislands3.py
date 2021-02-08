"""
Leetcode - 200. Number of Islands

input: grid w/ 1s and 0s. 1s being land
output: num - number of islands

Thoughts:
going to loop through the grid, when hit 1, call a helper function
do a depth first search looking at adjacent squares
if 1, keep calling the function, else, return nothing -- base case
mark the squares that we see w/ marker like "!"
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
print(numIslands(grid2))
