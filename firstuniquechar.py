"""
leetcode 387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""

# thoughts
# make a dictionary w/ letter(key) and counter? 
# loop through the string again
# if it's counter is 1, return the idx
# outside loop, return -1

def firstUniqChar(s):
    counter = {}
    
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
        
    for idx, letter in enumerate(s):
        if counter[letter] == 1:
            return idx
    
    return -1