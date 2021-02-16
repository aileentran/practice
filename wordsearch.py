"""
Leetcode - 79. Word Search

input: grid of letters, string that we're looking for
output: boolean - true if in board, false otherwise

Notes:
words constructed by adjacent letters
adjacent = vertical/horizontal
cannot reuse letters

Thoughts:
loop though board and find first letter
then dfs

mark the ones we've seen that matches the word
once we find all the letters, return true

if we don't make the word, prob need to use the old version
if reach end of the board, return false
"""

def exist(board, word):
    for r, row in enumerate(board):
        print('row', row)
        for c, col in enumerate(row):
            if col == word[0]:
                print('first letter', col)
                return dfs(word, board, r, c)
                # TODO: be able to return true after reaching the end of the word
                # TODO: if word isn't in board, continue looping through clean board for next letter 

    return False

def dfs(word, board, r, c):
    print(board)
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return

    if board[r][c] not in word:
        return False

    for letter in word:
        if board[r][c] == letter:
            board[r][c] = '!'
            dfs(word, board, r - 1, c)
            dfs(word, board, r + 1, c)
            dfs(word, board, r, c - 1)
            dfs(word, board, r, c + 1)

    # returning True no matter what.. hmmm...
    # TODO: return true once reach end of the word and it is in the board
    return True

board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
#True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
#True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"

print(exist(board1, word1))
# print(exist(board2, word2))
# print(exist(board3, word3))
