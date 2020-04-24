"""
input: two strings
output: int - # of char deleted to make anagram

anagram = string with the same letters & same num of letters

thoughts: hmm.. not string manipulation though.. :/ 
choose the shorter string to make a dictionary out: key - letters, val - # of letters
counter for deletions set to 0 

loop through longer string
if letter NOT in dict OR val of letter is 0-> counter += 1
if letter is in dict -> dict[letter] -= 1

outside of loop
return counter

TEST CASE:
consider leftover MULTIPLES of same letter
input: 
a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

output: 30

"""

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	shorter = min(a, b)
	longer = max(a, b)

	if shorter == longer:
		shorter = a
		longer = b

	shorterCount = {}

	for letter in shorter:
		if letter not in shorterCount:
			shorterCount[letter] = 1
		else:
			shorterCount[letter] += 1

	deletions = 0

	for letter in longer:
		if letter not in shorterCount or shorterCount[letter] == 0:
			deletions += 1
		else:
			shorterCount[letter] -= 1

	for letter in shorterCount:
		if shorterCount[letter] != 0:
			deletions += shorterCount[letter]

	return deletions