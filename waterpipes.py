"""
See if water can flow through!

input: grid; 0 = pipe, 1 = wall
output: boolean - True if water can flow from top to bottom
water can only move down, left, or right!
"""
# clear path
good = [
 [0, 0, 1, 1],
 [1, 0, 1, 1],
 [1, 0, 1, 1]
]

good2 = [
 [0, 1, 0, 1],
 [1, 0, 0, 1],
 [0, 0, 0, 0]
]

good3 = [
 [0, 0, 1, 0],
 [1, 0, 0, 1],
 [0, 0, 0, 0]
]

split = [
 [1, 0, 1, 0],
 [0, 0, 0, 0],
 [0, 1, 0, 1],
 [0, 1, 0, 1],
 [0, 1, 0, 1],
 [1, 1, 0, 1]
]

split2 = [
 [1, 1, 0, 1, 1],
 [0, 0, 0, 0, 0],
 [0, 1, 0, 1, 0],
 [0, 1, 1, 1, 0],
 [0, 1, 1, 1, 0],
 [1, 1, 1, 1, 0]
]

# blocked at top
top_blocked = [
 [1, 1, 1, 1],
 [1, 0, 0, 1],
 [0, 0, 0, 0]
]

# blocked at bottom
bottom_blocked = [
 [1, 0, 0, 1],
 [0, 0, 1, 1],
 [1, 1, 1, 1]
]

# diagonal between 1st and 2nd row
diagonal = [
 [0, 1, 1, 1],
 [1, 0, 1, 1],
 [1, 0, 0, 1]
]

# thoughts
# find the starting positions = 0s in first row
# have visited
# at the start
# check directions
# make sure directions are in bounds
# have dict for direction tuple AND 0 or 1 (pipe/wall)

# check to see if any of the things around are pipes
# if run into pipe, break check
# if no pipes, return false

# then loop  through directions dictionary
# if there is a pipe and direction is nOT in visted: set current to that direction
# append it into visited

def waterpipes(grid):
    """Check if there is a path for water to flow!"""
    nrows = len(grid)
    ncols = len(grid[0])

    # check for entire walls = fail early 
    for row in grid:
        if 0 not in row:
            return False 

    start = []
    visited = []

    for i, col in enumerate(grid[0]):
        if col == 0:
            start.append((0, i))
    # print(start)
    
    pos = start.pop()
    row, col = pos
    print('before', start)
    while True:
        # print('position', (row, col))
        print('start', start)
        # at the bottom of grid!
        if row == len(grid) - 1:
            break

        visited.append((row, col))
        # set up directions!
        down = (row + 1, col)
        left = (row, col - 1)
        right = (row, col + 1)

        directions = [down, left, right]
        
        pipe_or_wall = {}
        # check if directions are in bounds
        for direction in directions:
            row, col = direction 
            
            if (row >= 0) and (row < nrows) and (col >= 0) and (col < ncols):
                pipe_or_wall[direction] = grid[row][col]

        any_pipes = False

        for direction in pipe_or_wall:
            if pipe_or_wall[direction] == 0:
                any_pipes = True

        # no where for the water to flow!
        if not any_pipes and len(start) > 0:
            row, col = start.pop()

        elif not any_pipes:
            return False

        # print(pipe_or_wall)
        # print('visited', visited)

        for direction in pipe_or_wall:
            if pipe_or_wall[direction] == 0 and direction not in visited:
                start.append(direction)
                row, col = direction
                break



   



        

    return True

# print(waterpipes(good)) #True
# print(waterpipes(top_blocked)) #False
# print(waterpipes(bottom_blocked)) #False
# print(waterpipes(diagonal)) #False
print(waterpipes(good2)) #True
print(waterpipes(good3)) #True
print(waterpipes(split)) #True
print(waterpipes(split2)) #True