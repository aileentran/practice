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
    islands = 0

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "1":
                dfs(grid, r, c)
                islands += 1  #counting first time run dfs

    return islands

def dfs(grid, r, c):
    if r < 0 or c < 0  or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
        return
    grid[r][c] = "!"
    dfs(grid, r + 1, c) #up
    dfs(grid, r - 1, c) #down
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
