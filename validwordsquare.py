# input: list of words/strings
# output: boolean - true if row[i] == col[i]; false otherwise

# Clarifying Q's: 
# would ever get anything besides strings? 
# chars only? 
# same num of rows and cols?

# thoughts
# row = words[i]
# col1 = words[0][0], words[1][0], words[2][0], words[3][0]
# col2 = words[0][1], words[1][1], words[2][1], words[3][1]
# col3 = words[0][2], words[1][2], words[2][2], words[3][2]
# col4 = words[0][3], words[1][3], words[2][3], words[3][3]

# make an array of cols?

# while loop through both words and cols
# check if each element matches
# if not, false

# outside loop, return true!

def validWordSquare(words):
    """Check if valid word square where row[i] == col[i]."""
    cols = []

    i = 0

    while i < len(words):
        s = ''
        k = 0

        while k < len(words[i]):
            col_char = words[k][i]
            s += col_char
            k += 1

        cols.append(s)

        i += 1

    l = 0 

    while l < len(words):
        row = words[l]
        col = cols[l]

        if row != col: #secret loop under the hood in Python!
            return False 

        l += 1

    return True

# runtime: O(i * k) + O(l * n) --> O(n^2) + O(n^2) --> O(2n^2) --> O(n^2)
# runspace: n = length of words; c = num of chars --> c = n --> n * n --> n^2
# cols becomes length n 

# c = 'aaa' + 'bbb' 

print(validWordSquare([
   "abcd",
   "bnrt",
   "crmy",
   "dtye"
 ])) #true

print(validWordSquare([
   "abcd",
   "bnrt",
   "crm",
   "dt"
 ])) #true

print(validWordSquare([
   "ball",
   "area",
   "read",
   "lady"
 ])) #false bc row1 != col1 row3 != col3 

print(validWordSquare([
    "ball",
    "asee",
    "let",
    "lep"])) #false

