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
    return

board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
#True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
#True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
