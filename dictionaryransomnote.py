"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""

# Notes
# case sensitive and must use whole words
# can only use words once
# input: list of words from magazine, list of words for note
# output: Yes if can make ransom note, No if not

# fail early
# if magazine length < note: return No

# loop through magazine words and make a counter
# loop through note and reduce counter in magazine
# if at any point counter is 0 OR word is NOT in magazine, return No

# outside loop, return yes

def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        print('No')
        return 
    
    magazine_counter = {}
    for word in magazine:
        if word not in magazine_counter:
            magazine_counter[word] = 1
        else:
            magazine_counter[word] += 1
    
    for word in note:
        if word not in magazine_counter or magazine_counter[word] < 1:
            print('No')
            return
        elif magazine_counter[word]:
            magazine_counter[word] -= 1
    
    print('Yes')

# run time: O(m) in first loop where m = len(magazine)
# run time: O(n)in second loop where n = len(note), 
# run time: hidden loop of O(mc) where mc = len(magazine_counter)
# run time = O(m) + (O(n) * O(mc)) ~> O(n2)

# run space: magazine counter -> O(m) 



######################################################
# Old attempt
def checkMagazine(magazine, note):
    mag = {}

    for word in magazine:
        if word in mag:
            mag[word] += 1
        else:
            mag[word] = 1


    for word in note:
        if word in mag and mag[word] > 0:
            mag[word] -= 1
        else:
            print("No")
            return

    print("Yes")