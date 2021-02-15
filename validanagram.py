"""
Leetcode - 242. Valid Anagram

input: two strings
output: boolean - true if valid anagrams of each other

thoughts
sort both strings in alphabetical order
see if they are equal - true if equal, false if not
"""

def isAnagram(s, t):
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if s == t:
        return True
    return False

s1 = "anagram"
t1 = "nagaram"
#True

s2 = "rat"
t2 = "car"
#False

print(isAnagram(s1, t1))
print(isAnagram(s2, t2))
