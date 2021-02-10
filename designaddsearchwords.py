"""
Leetcode - 211. Design Add and Search Words Data Structure

input: list of words
output: results based on which methods called

Notes:
methods to: add words, search words
search words - '.' can replace any character
"""

# class Trie():
#     def __init__(self):
#         self.head = {}

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

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.head

        # compare character to current
        for char in word:
            # character is a letter but does not match current node
            if char != '.' and char not in curr:
                return False
            # character is '.' and need to do dfs through Trie
            elif char == '.':
                # wild_card = curr
                # curr = curr[wild_card]
            # character is a letter AND matches current node
            else:
                curr = curr[char]

    def dfs(self, word, curr):
        return

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
# wordDictionary.search("pad") # return False
# wordDictionary.search("bad") # return True
# wordDictionary.search(".ad") # return True
# wordDictionary.search("b..") # return True
