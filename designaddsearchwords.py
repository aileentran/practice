"""
Leetcode - 211. Design Add and Search Words Data Structure

input: list of words
output: results based on which methods called

Notes:
methods to: add words, search words
search words - '.' can replace any character
"""

class Trie():
    def __init__(self):
        self.head = {}

class WordDictionary(object):
    def __init__(self):
        self.head = Trie()

    def addWord(self, word):
        curr = self.head

        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr['*'] = True

    def search(self, word):
        curr = self.head

        for char in word:
            if char == '.':
                self.dfs(word, curr)

    def dfs(self, word, curr):
        return

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad") # return False
wordDictionary.search("bad") # return True
wordDictionary.search(".ad") # return True
wordDictionary.search("b..") # return True
