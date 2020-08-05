"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
"""

# input: string of words
# output: boolean - true if valid capitalization, false otherwise

# thoughts
# make a string of capital letters
# counter = length of string

# loop through string
# if encounter capital, subtract from counter

# outside loop
# if counter -1 OR 0 OR no change, return true
# else return false

# def determine_capital(string):

#     capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lowercase_counter = len(string)

#     for letter in string:
#         if letter in capitals:
#             lowercase_counter -= 1

#     if lowercase_counter == len(string) - 1 or lowercase_counter == 0 or lowercase_counter == len(string):
#         return True 
#     else:
#         return False


# space complexity: O(1)
# capitals = O(26) -> O(1)
# lowercase_counter = O(len(string)) -> O(1)

# run time: O(n^2)
# for loop -> O(n)
# if letter in capitals: hidden loop = O(c) -> O(n)

###################################

# no caps = true
# ALL caps = true
# ONLY first letter cap = true
# need to keep track of number of capital letters AND position!


# thoughts
# string of capitals
# empty list for capitals - > boolean values

# loop through string
# if letter in capitals list -> append true
# else append false 

# first cap = caps list[0]
# if first cap == false
# loop through list, if encounter true = return false

# if first cap == true and list[1] == true
# loop through list  
# if encounter false, return false

# if fist cap == true and list[1] == false
# loop through list starting at second letter
# if encounter true, return false

def determine_capital(string):
    all_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caps_list = []

    for letter in string:
        if letter in all_caps:
            caps_list.append(True)
        else:
            caps_list.append(False)

    first_cap = caps_list[0]
    sec_cap = caps_list[1]

    # all lowercase string
    if first_cap == False:
        for cap in caps_list:
            if cap == True:
                return False

    # capitalized word
    if first_cap == True and sec_cap == False:
        i = 1
        while i < len(caps_list):
            capitalized = caps_list[i]
            if capitalized == True:
                return False
            i += 1

    # all caps
    if first_cap == True and sec_cap == True:
        for cap in caps_list:
            if cap == False:
                return False

    return True


print(determine_capital("USA")) #true
print(determine_capital("FLaG")) #false
print(determine_capital("Google")) #true
print(determine_capital("bLue")) #false


