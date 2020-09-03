""" 
Leetcode challenge 9/3/2020 

Given a non-empty string check if it can be constructed by taking a
substring of it and appending multiple copies of the substring
together. You may assume the given string consists of lowercase
English letters only and its length will not exceed 10000  

"""
# Thoughts
# input: string of lowercase letters
# output: boolean - True if repeated substring, False otherwise

# empty string
# loop through string
# add to empty string until hit the same letter again
# now have substring

# slice string and save to array
# loop through the array and see if they all match substring
# false if encounter something that doesn't match

# outside loop
# return true 

def repeated_substring_pattern(string):
    substring = ""

    for letter in string:
        if letter not in substring:
            substring += letter

    i = 0

    while i < len(string):
        sliced_string = string[i: i + len(substring)]

        if sliced_string != substring:
            return False

        i += len(substring)

    return True

# Tests
print(repeated_substring_pattern("abab")) 
# Output: True
# Explanation: It's the substring "ab" twice.

print(repeated_substring_pattern("aba"))
# Output: False

print(repeated_substring_pattern("abcabcabcabc"))
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

# considerations: 
# substring has repeated letters -> "abcad" or "acdc" or "abcabd" etc. 
# what about one letter?