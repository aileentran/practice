# reverse the message! 
# input: list of characters
# output: string 

# main idea: reverse all the characters -> words are still reversed
# reverse the individual words
# join the words into a string! 

# reversing all characters -> similar to reversing in place
# left index, right index, middle index
# need to import math to do the math.ceil thing

# while loop left idx < middle index
# swap the characters with the nifty list[left], list[right] = list[right], list[left]

# reverse characters in individual words
# how.. to determine when we run into a word
# a word is indicated when the next val is space 
# keep track of left idx of word
# keep track of right idx of word
# reverse the characters

# then go to the next word

# new left idx is the one after the space 
# new right idx is right before the next space
# end is the end of the list 

# hmm.. well. time to get started!

# import math

def reverse_words(message):

    # Decode the message by reversing the words

    left_idx = 0
    right_idx = -1
    middle_idx = len(message) // 2

    while left_idx <= middle_idx:
    	message[left_idx], message[right_idx] = message[right_idx], message[left_idx]

    	left_idx += 1
    	right_idx -= 1

    # now message is completely reversed. words are backwards too 
    print(message)

    left_letter = 0
    right_letter = 0
    middle_letter = 0
    idx = 0

    while idx <= len(message):


    	if message[idx] == ' ' or idx == len(message) - 1:
    		right_letter = idx - 1
    		middle_letter = idx // 2

    		print(message[left_letter])
    		print(message[middle_letter])
    		print(message[right_letter])
    		
    		# reverse the word's characters
    		while left_letter <= middle_letter:
    			message[left_letter], message[right_letter] = message[right_letter], message[left_letter]

    			left_letter += 1
    			right_letter -= 1

    		# left letter is idx + 1 after the space 
    		# print('next left letter', message[left_letter])
    		print(message)


    	idx += 1
    	left_letter = idx

    return message

