"""
leveret in a garden (grid)
start: in the middle. if 2 cells in middle, starts in cell w/ more carrots 
looks WNES to find the cell with the most carrots
if tie for num of carrots, go for cell in WNES order
stop: no carrots in surrounding cells 

input: garden - 2D matrix w/ ints 
output: num of carrots eaten 

garden[row][col]
west = [row][col - 1]
north = [row - 1][col]
east = [row][col + 1]
south = [row + 1][col]

helper func -> find the center and have the leveret start there

main func 
feed garden into center func to get starting point 
empty carrots counter
make empty list for carrots or dictionary..?
dictionary: dir[key]: num carrots [value]

while west, north, east, south (are NOT 0):
    peek into WNES and append into list of carrots 
    pick the one with the most value
    if tie, move in WNES precedence
    add value to carrots counter
    set val in that position to 0
    change position in that direction

return carrots counter

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



    