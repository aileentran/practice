"""
Attempt 3 w/dfs method

input: garden - 2d grid of nums
output: num - total number of carrots eaten before leveret falls asleep

Notes
Start in the middle (largest number of carrots if multiple "middles")
Look WNES and go to one with the largest num of carrots
If tie, go to the one in direction order

Thoughts
helper function to find the middle/starting point
main function - counter for carrots and dfs?
hit base case of 0s around the leveret = return carrot count
"""

def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    start = center(garden, nrows, ncols)
    print(start)



def center(garden, nrows, ncols):
    center_squares = []
    row_idxs = []
    col_idxs = []
    start = None
    carrots = 0

    row_idxs.append(nrows // 2)
    col_idxs.append(ncols // 2)

    if nrows % 2 == 0:
        row_idxs.append(nrows // 2 - 1)

    if ncols % 2 == 0:
        col_idxs.append(ncols // 2 - 1)

    for row in row_idxs:
        for col in col_idxs:
            center_squares.append((row, col))

    if len(center_squares) == 1:
        return center_squares[0]

    for square in center_squares:
        row, col = square
        if garden[row][col] > carrots:
            start = (row, col)
            carrots = garden[row][col]

    return start





garden1 = [
    [1, 1, 1],
    [0, 1, 1],
    [9, 1, 9]
] #3

garden2 = [
    [9, 9, 9, 9],
    [9, 3, 1, 0],
    [9, 1, 4, 2],
    [9, 9, 1, 0]
] #6

garden3 = [
    [2, 3, 1, 4, 2, 2, 3],
    [2, 3, 0, 4, 0, 3, 0],
    [1, 7, 0, 2, 1, 2, 3],
    [9, 3, 0, 4, 2, 0, 3]
] #15

print(lunch_count(garden1))
print(lunch_count(garden2))
print(lunch_count(garden3))
