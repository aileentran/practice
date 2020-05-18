"""
input: string of letters
output: int - num of deletions so that chars don't repeat 
"""

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0

    i = 0
    while i < len(s) - 1:
        curr = s[i]
        nex = s[i + 1]

        if curr == nex:
            deletions += 1

        i += 1

    return deletions


# tests
print(alternatingCharacters('AAAA')) # 3 deletions -> A
print(alternatingCharacters('BBBBB')) # 4 deletions -> B
print(alternatingCharacters('ABABABAB')) # 0 deletions -> ABABABAB
print(alternatingCharacters('BABABA')) # 0 deletions -> BABABA
print(alternatingCharacters('AAABBB')) # 4 deletions -> AB