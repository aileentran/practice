"""
See if water can flow through!

input: grid; 0 = pipe, 1 = wall
output: boolean - True if water can flow from top to bottom
water can only move down, left, or right!
"""
# clear path
good = [
 [1, 0, 0, 1],
 [1, 0, 1, 1],
 [1, 0, 1, 1]
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

def waterpipes(grid):
    """Check if there is a path for water to flow!"""
    visited = []
    
    pos = []

    for i,row in enumerate(grid):
        if 0 not in row:
            return False

        print('row', row)
        # print('row idx', i)
        for k, col in enumerate(row):
            visited.append((i, k))
            print('col', col)
            # print('col idx', k)
            val = grid[i][k]
            # print('val', val)
            if val == 0:
                pos.append((i, k))

    # down = [row + 1][col]
    # left = [row][col - 1]
    # right = [row][col + 1]
    
    # for p in pos:
    #     row, col = p 


    print(pos)
    # print(visited)

    return True

print(waterpipes(good)) #True
# print(waterpipes(top_blocked)) #False
# print(waterpipes(bottom_blocked)) #False
# print(waterpipes(diagonal)) #False