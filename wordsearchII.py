"""
Leetcode - 212. Word Search II

input: board, list of words to look for
output: list of words found from given list

Notes:
letters must be adjacent and only used once for given word
"""

def findWords(board, words):
    return 

board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

board2 = [["a","b"],["c","d"]]
words2 = ["abcb"]
# Output: []

print(findWords(board1, words1))
print(findWords(board2, words2))
