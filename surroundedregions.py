"""
Leetcode - 130. Surrounded Regions

input: grid w/ 'x' and 'o'
output: grid w/all surrounded 'o's flipped to 'x'

NOT surrounded = o's and those adj at the BORDER are not flipped
surrounded = o's and adj o's NOT at border are flipped
"""

def solve(board):
    # checking for O's connected to border
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            # O's along border, mark w/ '!'
            if col == 'O' and (r == 0 or r == len(board) - 1 or c == 0 or c == len(row) - 1):
                border_dfs(board, r, c)

    # check for surrounded O's
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == 'O':
                surrounded_dfs(board, r, c)

    # check for '!' and convert to O's
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == '!':
                board[r][c] = 'O'
    return board

def surrounded_dfs(board, r, c):
    #consider borders here in base case
    if r < 1 or c < 1 or r >= len(board) - 1 or c >= len(board[0]) - 1 or board[r][c] != 'O':
        return
    board[r][c] = 'X'
    surrounded_dfs(board, r - 1, c)
    surrounded_dfs(board, r + 1, c)
    surrounded_dfs(board, r, c - 1)
    surrounded_dfs(board, r, c + 1)

def border_dfs(board, r, c):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != 'O':
        return
    board[r][c] = '!'
    border_dfs(board, r - 1, c)
    border_dfs(board, r + 1, c)
    border_dfs(board, r, c - 1)
    border_dfs(board, r, c + 1)

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
print(solve(board1))
print(solve(board2))
