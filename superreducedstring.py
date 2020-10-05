"""
Hackerrank - Super Reduced String
Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String


"""

def superReducedString(s):
    stack = []

    for i, char in enumerate(s):
    	if stack and char == stack[-1]:
    		stack.pop()
    	else:
    		stack.append(char)
    
    if len(stack) == 0:
    	return 'Empty String'

    return ''.join(stack)

# tests
s1 = 'aaabccddd' #abd
s2 = 'aa' #Empty String
s3 = 'baab' #Empty String; currently getting 'bb'

print(superReducedString(s3))







##########################
def superReducedString1(s):
    i = 0

    while i < len(s):
        print('s @ start of loop', s)
        char1 = s[i]
        char2 = s[i + 1]
        print('char1', char1)
        print('char2', char2)
        if char1 == char2:
            print('match!')
            s = s[:i] + s[i + 2:]
            # print(s)
        i += 1

    if len(s) == 0 or s[0] == s[1]:
        return 'Empty String'
    return s