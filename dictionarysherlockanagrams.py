"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""

# Notes and thoughts
# input: string
# output: integer - number of anagrammatic pairs
# anagram = the same number of letters in any order

# maybe make a helper function that MAKES the substrings?
# ^creates all possible substrings

# main function, compare the substrings and make pairs

# find repeated letters
# find the letters around it to make 2+ length anagrams

# hmm.. seems to be more of a looped slicing for 2+ letters

# OR A DICTIONARY CONTAINING ALL OF THE SLICESSS! 
# a dictionary with beginning slices and a dictionary for end slices
# then going through both dictionaries and search for its slices..? 
# or one dictionary with.. key being beginning of string slicey thing and value is the tail 

# OR ANOTHER DICTIONARY WITH MATCHED LETTERS AND IDXS??
# hmm.. key = idx and value = matched letters..?
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagram_pair = []
    idx_matched_letters = []
    matched_letters = {}
    head_tail_substrings = {}      
    counter = 0

    # finding repeated letters
    i = 0
    while i < len(s) - 1:
        curr_letter = s[i]
        k = i + 1
        while k < len(s):
            next_letter = s[k]
            if curr_letter == next_letter:
                matched_letters[curr_letter] = [i, k]
                # anagram_pair.append([curr_letter, next_letter])
                # idx_matched_letters.append([i, k])
                counter += 1
            k += 1
        i += 1
    # print(anagram_pair)
    print(matched_letters)

    # if can't even find duplicate letters, it's a no go!
    if len(matched_letters) == 0:
        return 0

    # finding 2+ anagrams 
    # AROUUNNNDDD matched letters  
    # hmm.. between first matched letter and second matched letter?
    for letter in matched_letters:
        idx1, idx2 = matched_letters[letter]
        print('idx1', idx1)
        print('idx2', idx2)

        i = idx1
        while i < idx2:
            head = sortedString(s[:i + 1])
            tail = sortedString(s[i + 1: idx2 + 1])

            print('head', head)
            print('tail', tail)
            if head not in head_tail_substrings:
                head_tail_substrings[head] = 1
            else:
                head_tail_substrings[head] += 1
            
            if tail not in head_tail_substrings:
                head_tail_substrings[tail] = 1
            else:
                head_tail_substrings[tail] += 1

            print(head_tail_substrings)
            i += 1
    
    

def sortedString(letters):
    return ''.join(sorted(letters))

###################################
def sherlockSolution(s):
	n = len(s)
	pairs = 0

	for i in range(1, n): #length of substring
		# print('i', i)
		# print('s[i]', s[i])
		print('length of substring', i)
		substring_counter = {}

		for k in range(n - i + 1): #looping through string and staying within bounds
			# print('k', k)
			# print('k + i', k + i)
			print(s[k:k + i])
			substring = ''.join(sorted(s[k:k + i]))
			# print(substring)
			if substring not in substring_counter:
				substring_counter[substring] = 1
			else:
				substring_counter[substring] += 1

			pairs += substring_counter[substring] - 1

			print(substring_counter)
			print('adding pair', substring_counter[substring] - 1)
			print(pairs)
			print('\n')

	return pairs
# Tests
l1 = 'abba' # 4
l2 = 'abcd' # 0
l3 = 'ifailuhkqq' # 3
l4 = 'kkkk' # 10
l5 = 'cdcd' # 5
l6 = 'mom' # 2

print(sherlockSolution(l3))