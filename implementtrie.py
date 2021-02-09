"""
Leetcode - 208. Implement Trie (Prefix Tree)

Trie - a tree that holds strings - letters
"""

class Trie(object):
    def __init__(self):
        self.head = {}

    def insert(self, word):
        curr = self.head
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True
        return curr

    def search(self, word):
        """Returns True if the word is in trie."""
        curr = self.head
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        if "*" not in curr:
            return False
        else:
            return True

    def startsWith(self, prefix):
        """Returns true if a word starts with this prefix, false otherwise."""
        curr = self.head
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))   #// returns true
print(trie.search("app") )    #// returns false
print(trie.startsWith("app")) #// returns true
print(trie.insert("app"))
print(trie.search("app"))     #// returns true
