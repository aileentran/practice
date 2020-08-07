"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

"""
# thoughts
# set everything to lower case
# loop through string using while loop -> consider odd num of letters
# two pointers -> end and beginning
# if it is a letter, compare it
# otherwise, keep going until run into number
# if letters dont match return False

# outside loop
# return true

def is_palindrome(string):
    string.lower()

    f = 0
    b = -1

    while f < len(string):
        front = string[f]
        back = string[b]
        print('front', front)
        print('back', back)
        b -= 1
        f += 1

# print(is_palindrome("A man, a plan, a canal: Panama")) #true
# print(is_palindrome("race a car")) #false
print(is_palindrome('dog'))
print(is_palindrome('a dog'))