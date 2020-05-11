"""
input: str, idx of opened parentheses!
output: idx of paired parentheses 

a stack = list


while loop starting at idx of opening parentheses

an open parentheses = added in stack,  
a closed parentheses = pop stack 
when stack is empty, return idx! 
"""

def get_closing_paren(sentence, opening_paren_index):
	# stack of open parentheses!
	paren = []

	i = opening_paren_index

	while i < len(sentence):

		if sentence[i] == '(':
			paren.append(sentence[i])
		elif sentence[i] == ')':
			paren.pop()

		if len(paren) == 0:
			return i

		i += 1
	
	raise ValueError('No matching closing parentheses!')


