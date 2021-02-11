"""
Leetcode - 211. Design Add and Search Words Data Structure

input: list of words
output: results based on which methods called

Notes:
methods to: add words, search words
search words - '.' can replace any character
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.head

        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr['*'] = True
        # return self.head

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.head
        # print('self.head', self.head)
        # print('initial curr', curr)
        # compare character to current
        for c, char in enumerate(word):
            # print('char', char)
            # print('curr inside loop', curr)
            # character is a letter but does not match current node
            if char != '.' and char not in curr:
                return False
            # character is '.' and need to do dfs through Trie
            elif char == '.':
                return self.dfs(word, c, curr)
            else:
                curr = curr[char]

        if '*' in curr:
            return True
        else:
            return False

    def dfs(self, word, c, curr):
        if c >= len(word):
            if '*' in curr:
                return True
            else:
                return False

        for key, val in curr.items():
            if self.dfs(word, c + 1, val):
                return True
            return False

wordDictionary = WordDictionary()
print(wordDictionary.addWord("bad"))
print(wordDictionary.addWord("dad"))
print(wordDictionary.addWord("mad"))
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True
