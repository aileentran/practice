"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""
# Notes and thoughts
# input: two strings of letters
# see if they share a substring - even letters 
# loop through shorter string to safe on run time

# basically same as first attempt


########################################################
# First attempt awhile ago
def twoStrings(s1, s2):
    longer = max(s1, s2)
    short = min(s1, s2)

    for letter in short:
        if letter in longer:
            return "YES"
        
    return "NO"

# run time: O(s) * hidden inner loop O(l) = O(s) * O(l) ~ O(n2)
# run space: O(1) just established a couple of static variables