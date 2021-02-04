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
