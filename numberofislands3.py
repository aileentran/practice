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
    islands = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == '1':
                dfs(grid, r, c)
                islands += 1
    return islands

def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
        return
    grid[r][c] = "!"
    dfs(grid, r - 1, c) #up
    dfs(grid, r + 1, c) #down
    dfs(grid, r, c - 1) #left
    dfs(grid, r, c + 1) #right


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
