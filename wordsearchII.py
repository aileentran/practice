"""
Leetcode - 212. Word Search II

input: board, list of words to look for
output: list of words found from given list

Notes:
letters must be adjacent and only used once for given word
"""

class Trie(object):
    def __init__(self):
        self.head = {}

    def add(self, word):
        curr = self.head
        # print(curr)
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr['*'] = True
        # print(curr)

    def search(self, word):
        curr = self.head

        for char in word:
            if char not in curr:
                return False
            curr = curr[char]

        if '*' in curr:
            return True
        else:
            return False

    def prefix(self, word):
        curr = self.head

        for char in word:
            if char not in curr:
                return False
            curr = curr[char]

        return True


def findWords(board, words):
    found = []
    trie = Trie()

    for word in words:
        trie.add(word)

    head = trie.head
    print(head)
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col in head:
                dfs(board, r, c, head)
    return

def dfs(board, r, c, head):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return
    


board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

board2 = [["a","b"],["c","d"]]
words2 = ["abcb"]
# Output: []

print(findWords(board1, words1))
# print(findWords(board2, words2))
