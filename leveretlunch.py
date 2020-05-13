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
-dead center
-if multiple squares: highest number of carrots
empty list of potential starts
odd num: num // 2 = idx
even num: num // 2 = lower row or col; lower - 1 = upper row or col

list of carrot vals:
-append val @ [row][col]

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

TEST CASES:
garden = [
        [1, 1, 1],
        [0, 1, 1],
        [9, 1, 9]
        ]
starting position = (1, 1)

garden = [
    [9, 9, 9, 9],
    [9, 3, 1, 0],
    [9, 1, 4, 2],
    [9, 9, 1, 0]
    ]
starting position = (2, 2)


garden = [
    [2, 3, 1, 4, 2, 2, 3],
    [2, 3, 0, 4, 0, 3, 0],
    [1, 7, 0, 2, 1, 2, 3],
    [9, 3, 0, 4, 2, 0, 3]
    ]
starting position = (1, 3)
"""
def center(garden):
    """Given a garden, return the leveret's starting point."""
    nrows = len(garden)
    ncols = len(garden[0])

    midrow = []
    midcol = []

    if nrows % 2 != 0:
        ridx = nrows // 2
        midrow.append(ridx)
    else:
        lower = nrows // 2
        upper = lower - 1
        midrow.append(upper)
        midrow.append(lower)

    if ncols % 2 != 0:
        cidx = ncols // 2
        midcol.append(cidx)
    else:
        lower = ncols // 2 
        upper = lower - 1
        midcol.append(upper)
        midcol.append(lower)

    starts = []

    for row in midrow:
        for col in midcol:
            starts.append((row, col))

    most_carrots = 0
    starting_pos = None

    for start in starts:
        row = start[0]
        col = start[1]

        if garden[row][col] > most_carrots:
            most_carrots = garden[row][col]
            starting_pos = start


    return starting_pos


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

    start = center(garden)
    row, col = start

    print('start', start)
    
    total_eaten = 0

    while True:
        west = (row, col - 1)
        north = (row - 1, col)
        east = (row, col + 1)
        south = (row + 1, col)

        directions = [west, north, east, south]

        all_da_carrots = {}

        for direction in directions:
            if (direction[0] > nrows - 1) or (direction[0] < 0) or (direction[1] > ncols - 1) or (direction[1] < 0):
                # out of bounds and bunny doesn't care about no carrots
                all_da_carrots[direction] = 0
            else:
                all_da_carrots[direction] = garden[direction[0]][direction[1]]

        print(all_da_carrots)

        total_eaten += garden[row][col]
        garden[row][col] = 0

        any_carrots = False
        for pos in all_da_carrots:
            if all_da_carrots[pos] > 0:
                any_carrots = True
                break

        if not any_carrots:
            break

        most_carrots = 0

        for pos in all_da_carrots:
            if all_da_carrots[pos] > most_carrots:
                most_carrots = all_da_carrots[pos]
                row, col = pos
        
        if (row > nrows) or (row < 0) or (col > ncols) or (col < 0) :
            break

        print('next', (row, col))


    return total_eaten


garden1 = [
        [1, 1, 1],
        [0, 1, 1],
        [9, 1, 9]
        ]

garden2 = [
    [9, 9, 9, 9],
    [9, 3, 1, 0],
    [9, 1, 4, 2],
    [9, 9, 1, 0]
    ]


garden3 = [
    [2, 3, 1, 4, 2, 2, 3],
    [2, 3, 0, 4, 0, 3, 0],
    [1, 7, 0, 2, 1, 2, 3],
    [9, 3, 0, 4, 2, 0, 3]
    ]


print(lunch_count(garden1))
print(lunch_count(garden2))
print(lunch_count(garden3))