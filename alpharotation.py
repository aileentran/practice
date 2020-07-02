# input: list of words in alpha order! 
# output: idx of rotation point 

def find_rotation_point(words):

    # Find the rotation point in the list
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    floor = -1
    ceil = len(words)

    idx = 0

    for word in words:
        print(word)
        for char in word:
            print('char', char)
            i = 0

            while i < len(alpha):
                letter = alpha[i]
                print('letter', letter)
                # if char == letter:

                i += 1


print(find_rotation_point(['cape', 'cake'])) #1
# print(find_rotation_point(['grape', 'orange', 'plum','radish', 'apple'])) #4
# print(find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
#                                       'undulate', 'xenoepist', 'asymptote','babka', 'banoffee', 'engender','karpatka', 'othellolagkage'])) #5