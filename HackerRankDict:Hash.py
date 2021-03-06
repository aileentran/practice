"""
input: 2 arrays of strings - magazine array & ransom array
output: "Yes" or "No"

Yes = right words AND enough in magazine
No otherwise

THOUGHTS
make empty counter => dictionary 
iterate through magazine and add word as key and val as int

iterate through ransom array 
if word in magazine dictionary and count > 0
magazine[word] -= 1

else return "No"

outside loops
return "Yes"


TEST CASES
Input 1:
mag = ['give', 'me', 'one', 'grand', 'today', 'night']
ran = ['give', 'one', 'grand', 'today']

Output 1: Yes

Input 2:
mag = ['two', 'times', 'three', 'is', 'not', 'four']
ran = ['two', 'times', 'two', 'is', 'four']

Output 2: No - two in magazine once

Input 3: 
mag = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
ran = ['ive', 'got', 'some', 'coconuts']

Output 3: No - missing some


"""

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
	mag = {}

	for word in magazine:
		if word in mag:
			mag[word] += 1
		else:
			mag[word] = 1


	for word in note:
		if word in mag and mag[word] > 0:
			mag[word] -= 1
		else:
			return "No"

	return "Yes"

##############################################################
"""
input: 2 strings
output: return "Yes" if contain substrings (even letters), return "No" otherwise

find the longer word
loop through that and make a dictionary with letter as key and.. val as int?

loop through shorter word and see if it is in the dictionary.. 
why have a dictionary..?


"""

# Complete the twoStrings function below.
def twoStrings(s1, s2):
	longer = max(s1, s2)
	short = min(s1, s2)

	for letter in short:
		if letter in longer:
			return "Yes"
		
	return "No"

