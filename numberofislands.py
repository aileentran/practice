"""
Leetcode - Number of Islands

input: grid of 1s and 0s, 1 = land 0 = water
output: num - number of Islands

note
island = surrounded by water and connected by land vertically and horizontally
list of adjacent lands
list of seen
loop through cols until find 1, peek around it (up, down, left, right).
go through adjacent lands and see if
"""

def numIslands(grid):
    seen_lands = []
    islands = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            adj = []
            if col == "1":
                seen_lands.append((r, c))
                adj.append((r - 1, c))
                adj.append((r, c - 1))
                adj.append((r, c + 1))
                adj.append((r + 1, c))
                adj_lands = adjacentLands(adj, grid)
                new_lands = seenLands(seen_lands, adj_lands, grid)
                # i need to go through new lands and see if there is land around
                # and.. need to keep looping through newlands until there ARENT any
                # then we have an island
                # almost feels like recursion but.. 
                # if there is land, add to new_lands
                # if new_lands is 0 == island so we increment island
                print('curr_land', (r, c))
                print('seen', seen_lands)
                print(new_lands)
                if len(new_lands) == 0:
                    islands += 1

    return islands

def adjacentLands(adj, grid):
    """Check for adjacent lands."""
    valid = validIndices(adj, grid)
    adj_lands = []
    for val in valid:
        r, c = val
        if grid[r][c] == "1":
            adj_lands.append(val)
    return adj_lands

def validIndices(adj, grid):
    """Check if adjacent indices are valid."""
    rows = len(grid)
    cols = len(grid[0])
    within_grid = []
    for a in adj:
        r, c = a
        if r in range(rows) and c in range(cols):
            within_grid.append(a)
    return within_grid

def seenLands(seen_lands, adj_lands, grid):
    """Check if adjacent lands are new."""
    new_lands = []
    for adj in adj_lands:
        if adj not in seen_lands:
            new_lands.append(adj)
    return new_lands

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
