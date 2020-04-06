# input: list of strings
# output: list of strings

# reverse string in place - need to use array bc python strings are immutable! 

# thoughts
# save the last item in a variable 
# OH! assuming items are unique!

# use a while loop 
# until the item is equal to the last item in the string
# remove first item and append to the end 
# NOPee

# oh its kinda like.. checking for a palindrome? 
# maybe.. using a for loop with enumerate 
# or while loop until we hit the middle item?? what about odd and even numbered lists..? hmm.. 
# 
# set var for first item and last item 
# OR POP OFF THE ITEMS! 
# first item -> append to end of list
# last item -> insert(0, last item)
# iterate 

# return the list thang 
import math

def reverse(list_of_chars):
	"""Reversing items in a list in place."""
	left_idx = 0
	right_idx = -1
	middle_idx = math.ceil(len(list_of_chars) / 2)
	print(middle_idx)


	while left_idx < middle_idx:

		print('left', list_of_chars[left_idx])
		print('right', list_of_chars[right_idx])

		list_of_chars[left_idx], list_of_chars[right_idx] = list_of_chars[right_idx], list_of_chars[left_idx]

		print(list_of_chars)
		left_idx += 1
		right_idx -= 1

	return list_of_chars