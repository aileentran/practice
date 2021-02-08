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
    return

    
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
