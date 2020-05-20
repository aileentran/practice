"""
input: garden - 2D array
output: num - total number of carrots eaten 

start in center: DEAD center OR if multiple centers, grid with the most carrots

helper function - finding center
input: garden grid
output: (row, col) of start
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
    nrow = len(garden)
    ncol = len(garden[0])

    row_idx = []
    col_idx = []

    if nrow % 2 != 0:
        row_idx.append(nrow // 2)
    else:
        row_idx.append((nrow // 2) - 1)
        row_idx.append(nrow // 2)

    if ncol % 2 != 0:
        col_idx.append(ncol // 2)
    else:
        col_idx.append((ncol // 2) - 1)
        col_idx.append(ncol // 2)
        

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

# def lunch_count(garden):


print(center(garden1)) # start: (1, 1)
print(center(garden2)) # start: (2, 2)
print(center(garden3)) # start: (1, 3)
# print(lunch_count(garden1)) # eaten: 3
# print(lunch_count(garden2)) # eaten: 6
# print(lunch_count(garden3)) # eaten: 15