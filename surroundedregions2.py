"""
Leetcode - 130. Surrounded Regions

input: grid of Xs and Os.
output: grid with surrounded Os flipped except ones connected to the boundary

Thoughts
loop through the grid and find all the Os connected to boundary and mark them - "!"
loop through new grid and flip the surrounded Os
loop through grid and convert "!" to Os
return the grid
"""
def solve(board):
    # looping through and finding Os along boundaries
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            # O's along boundaries + adjacent
            if col == 'O' and (r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1):
                boundary_dfs(board, r, c)

    # finding surrounded Os
    # MUST be in separate loop or else surrounded Os connected to boundary preemptive flip to X
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == 'O':
                flip_dfs(board, r, c)

    # convert boundary '!'s to Os
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == '!':
                board[r][c] = 'O'

    return board

def boundary_dfs(board, r, c):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != 'O':
        return
    board[r][c] = '!'
    boundary_dfs(board, r - 1, c) #up
    boundary_dfs(board, r + 1, c) #down
    boundary_dfs(board, r , c - 1) #left
    boundary_dfs(board, r, c + 1) #right


def flip_dfs(board, r, c):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != 'O':
        return
    board[r][c] = 'X'
    flip_dfs(board, r - 1, c) #up
    flip_dfs(board, r + 1, c) #down
    flip_dfs(board, r , c - 1) #left
    flip_dfs(board, r, c + 1) #right


board1 = [
['X', 'X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'X', 'O', 'X'],
['X', 'O', 'X', 'X']
]

"""
Answer:
X X X X
X X X X
X X X X
X O X X
"""

board2 = [
['X', 'X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'O', 'O', 'X'],
['X', 'O', 'X', 'X']
]

"""
Answer:
X X X X
X O O X
X O O X
X O X X
"""
print('board1', solve(board1))
print('board2', solve(board2))
