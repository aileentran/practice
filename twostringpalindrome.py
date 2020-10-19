"""
Leetcode: 1616. Split Two Strings to Make Palindrome
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

"""
# thoughts
# palindrome = same forwards as it is backwards
# input: stringA, stringB
# split both strings at same index
# a pre + b suff OR b pre + a suff 
# if can form palindrome at any point return true
# output: True if can form palindrome, False if not


def checkPalindromeFormation(a, b):
    i = 0
    while i < len(a):
        a_pre = a[:i]
        a_suff = a[i:]
        b_pre = b[:i]
        b_suff = b[i:]
        
        print('a_pre:', a_pre, 'a_suff', a_suff)
        print('b_pre:', b_pre, 'b_suff', b_suff)
        
        print(isPalindrome(a_pre, b_suff))
        print(isPalindrome(b_pre, a_suff))
        # pal1 = a_pre + b_suff
        # pal2 = b_pre + a_suff
        
        # p = 0
        # while p < len(pal1):
        #     start = pal1[]
        #     p += 1
        
        # if is_palindrome(a_pre, b_suff) or is_palindrome(b_pre, a_suff):
        #     return True
        i += 1
    return False

def isPalindrome(pre, suff):
	whole = pre + suff
	print(whole)
    

# Tests
a1 = "x"
b1 = "y" 
#True

a2 = "abdef"
b2 = "fecab"
#True

a3 = "ulacfd"
b3 = "jizalu"
#True

a4 = "xbdef"
b4 = "xecab"
#False
print(checkPalindromeFormation(a2, b2))
