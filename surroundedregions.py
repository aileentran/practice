"""
Leetcode - 130. Surrounded Regions

input: grid w/ 'x' and 'o'
output: grid w/all surrounded 'o's flipped to 'x'

NOT surrounded = o's and those adj at the BORDER are not flipped
surrounded = o's and adj o's NOT at border are flipped
"""

def solve(board):
    return

board = [
['X', 'X', 'X', 'X']
['X', 'O', 'O', 'X']
['X', 'X', 'O', 'X']
['X', 'O', 'X', 'X']
]

"""
Answer:
X X X X
X X X X
X X X X
X O X X
"""

print(solve(board))
