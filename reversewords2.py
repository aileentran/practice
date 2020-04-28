"""
input: array of words
output: string -> words in reversed order

thoughts:
array of words -> letters are in order but words are reversed 
currently know how to reverse letters

reverse entire array -> helper function
input: message, left idx, right idx
left idx and right idx (right idx CANNOT BE NEGATIVE!!)
loop til the middle: left > right
swap values left, right = right left 

return the array 

main function
left idx 

then loop through array and re-reverse the words 
words -> next item is a space OR the end of the list 
if run into space:
if space -> helper func(array, left idx, curr idx - 1)
left idx = cur idx + 1

if end of list: curr idx == len(array) - 1
helper func(array, left, curr idx)

outside loop
return joined array 

TEST CASE
input:  message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]

output: 'steal pound cake'

"""
# main func
def reverse_words(message):

    # Decode the message by reversing the words

    # reverse whole string 
    rev_chars(message, 0, len(message) - 1)

    # re-reverse the words
    l_idx = 0

    i = 0
    while i < len(message):
    	if message[i] == ' ':
    		rev_chars(message, l_idx, i - 1)
    		l_idx = i + 1
    	elif i == len(message) - 1:
    		rev_chars(message, l_idx, i)

    	i += 1

    return ''.join(message)

# helper func
def rev_chars(message, l_idx, r_idx):
	# reverse letters

	while l_idx < r_idx:
		message[l_idx], message[r_idx] = message[r_idx], message[l_idx]

		l_idx += 1
		r_idx -= 1

	return message



