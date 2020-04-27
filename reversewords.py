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
# test case
# input: array of letters
 # message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
 # output: string -> 'steal pound cake'

def reverse_words(message):

    # reverse entire message
    reverse_characters(message, 0, len(message) - 1)

    # reverse individual words
    left_idx = 0
    i = 0

    while i < len(message):
        if message[i] == ' ':
            reverse_characters(message, left_idx, i - 1)
            left_idx = i + 1
        elif i == len(message) - 1:
            reverse_characters(message, left_idx, len(message) - 1)

        i += 1


    return ''.join(message)

def reverse_characters(message, left_idx, right_idx):

    while left_idx < right_idx:
        message[left_idx], message[right_idx] = message[right_idx], message[left_idx]

        left_idx += 1
        right_idx -= 1

    return message
