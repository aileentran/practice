"""
input: string of LOWER CASE letters
output: boolean - true if palindrome; false if not

palindrome = word that is the same spelled forward or backwards
PERMUTATION -> word that has either even number of letters or only 1 odd number at most 

thoughts
dictionary as a counter for letters-> letter[key] : num[val]
loop through string and make a dictionary with counters 

odd num of letters counter = 0
go through dictionary 
if odd > 1 -> return false
if val is an odd num %2 != 0 -> odd += 1

outside loop: return true
"""

def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    letter_count = {}

    for letter in the_string:
    	if letter not in letter_count:
    		letter_count[letter] = 1
    	else:
    		letter_count[letter] += 1

    odd_num = 0

    for letter in letter_count: 
    	if letter_count[letter] % 2 != 0:
    		odd_num += 1

    if odd_num > 1:
    	return False

    return True