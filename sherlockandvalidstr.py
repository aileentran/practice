"""
input: str
output: "YES" if valid, "NO" if not

valid string = if all chars occur the same number of times 
OR if 1 char away from being valid 
"""



def isValid(s):
	char_count = {}

	for char in s:
		if char not in char_count:
			char_count[char] = 1
		else:
			char_count[char] += 1

	print(char_count)
	count = []

	for char in char_count:
		count.append(char_count[char])

	# number of diff counts; num of chars aka key in char_count [key]: total char types[value]

	num_count = {}

	for num in count:
		if num not in num_count:
			num_count[num] = 1
		else:
			num_count[num] += 1

	print('num_count', num_count)

	
	# all chars occur the same number of times 
	if len(num_count) == 1:
		return 'YES'

	# want diff of char occurences to be 1 away from mode
	# want it to only happen w/1 character
	mode = 0
	occurences = 0
	for num in num_count:
		if num_count[num] > occurences:
			occurences = num_count[num]
			mode = num
	

	for num in num_count:
		if ((num - 1 == mode) and num_count[num] == 1) or ((num == 1) and (num_count[num] == 1)):
			return 'YES'

	return 'NO'

	


# test cases
# print(isValid('aabbcd')) #NO
# print(isValid('aabbccddeefghi')) #NO
# print(isValid('abcdefghhgfedecba')) #YES
print(isValid('aabbc')) #YES
print(isValid('aaaabbcc')) #NO