"""
input: garden - 2D array
output: num - total number of carrots eaten 

start in center: DEAD center OR if multiple centers, grid with the most carrots

helper function - finding center
input: garden grid
output: (row, col) of start

main function
input: garden grid
output: int - total carrots 
"""

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

def center(garden):
    nrows = len(garden)
    ncols = len(garden[0])

    row_idx = []
    col_idx = []

    if nrows % 2 != 0:
        row_idx.append(nrows // 2)
    else:
        row_idx.append((nrows // 2) - 1)
        row_idx.append(nrows // 2)

    if ncols % 2 != 0:
        col_idx.append(ncols // 2)
    else:
        col_idx.append((ncols // 2) - 1)
        col_idx.append(ncols // 2)
        

    starts = []

    i = 0

    while i < len(row_idx):
        row = row_idx[i]
        k = 0

        while k < len(col_idx):
            col = col_idx[k]
            starts.append((row, col))
            k += 1

        i += 1


    # print(starts)
    most_carrots = 0
    start = starts[0]

    for s in starts:
        row, col = s
        carrots = garden[row][col]

        if carrots > most_carrots:
            most_carrots = carrots
            start = s

    return start

def lunch_count(garden):

    nrows = len(garden)
    ncols = len(garden[0])

    # find the center
    start = center(garden)
    # current position
    row, col = start

    total = 0

    while True:
        # eat the carrots at current position
        total += garden[row][col]
        # empty the carrots in current position
        garden[row][col] = 0

        # look at the diff directions WNES
        west = (row, col - 1)
        north = (row - 1, col)
        east = (row, col + 1)
        south = (row + 1, col)

        all_directions = [west, north, east, south]


        # dictionary of direction tuple(key) and # of carrots
        directions = {}

        # making sure within garden grid and fill in dictionary
        for direction in all_directions:
            dir_row, dir_col = direction
            if (dir_row < 0) or (dir_row >= nrows) or (dir_col < 0) or (dir_col >= ncols):
                directions[direction] = 0 #bunny will ignore 0 carrots
            else:
                directions[direction] = garden[dir_row][dir_col]
        
        # checking to there are carrots to eat in any direction!
        any_carrots = False

        for direction in directions:
            if directions[direction] > 0:
                any_carrots = True

        # no more carrots to eat
        if any_carrots == False:
            return total

        # checking which direction has the most carrots
        most_carrots = 0

        for direction in directions:
            if directions[direction] > most_carrots:
                most_carrots = directions[direction]
                row, col = direction






    

# print(center(garden1)) # start: (1, 1)
# print(center(garden2)) # start: (2, 2)
# print(center(garden3)) # start: (1, 3)
print(lunch_count(garden1)) # eaten: 3
print(lunch_count(garden2)) # eaten: 6
print(lunch_count(garden3)) # eaten: 15