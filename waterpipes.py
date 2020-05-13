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
 [1, 0, 0, 1]
 [0, 0, 1, 1]
 [1, 1, 1, 1]
]

# diagonal between 1st and 2nd row
diagonal = [
 [0, 1, 1, 1]
 [1, 0, 1, 1]
 [1, 0, 0, 1]
]

def waterpipes(grid):
    """Check if there is a path for water to flow!"""

    return True

print(waterpipes(good)) #True
print(waterpipes(top_blocked)) #False
print(waterpipes(bottom_blocked)) #False
print(waterpipes(diagonal)) #False