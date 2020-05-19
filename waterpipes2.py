"""
practicing water and pipes once more! 
see if water can flow from top to bottom of grid 
input: 2D array/grid
output: boolean
"""

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

def waterflow(grid):
    """Check if water canflow from top to bottom"""

    