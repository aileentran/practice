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
        for c, col in enumerate(row):
            print('row, col', row, col)
            print('original board', board)
            if dfs(word, board, r, c, 0):
                return True
    return False

def dfs(word, board, r, c, i):
    if i == len(word):
        return True

    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return

    if board[r][c] != word[i]:
        return False

    print('idx', i)
    print('current board letter', board[r][c])
    print('letter in word', word[i])
    #tmp allows us to use one board without needing to make a copy!
    original_value = board[r][c] #currently saving original board[r][c] value
    board[r][c] = '!'

    print('board after', board)
    print('\n')

    result = dfs(word, board, r, c + 1, i + 1) \
    or dfs(word, board, r + 1, c, i + 1) \
    or dfs(word, board, r, c - 1, i + 1) \
    or dfs(word, board, r - 1, c, i + 1)
    board[r][c] = original_value #returning board[r][c] to original value
    return result



board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
#True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
#True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"

board4 = [["C","A","A"],["A","A","A"],["B","C","D"]]
word4 = "AAB"
# True

board5 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word5 = "ABCESEEEFS"

board6 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word6 = "ABCEFSADEESE"

# print(exist(board1, word1))
# print(exist(board2, word2))
# print(exist(board3, word3))
# print(exist(board4, word4))
# print(exist(board5, word5))
print(exist(board6, word6))
