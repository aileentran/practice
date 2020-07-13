# input: list of words/strings
# output: boolean - true if row[i] == col[i]; false otherwise

# Q's: would ever get anything besides strings? chars only?

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
    w = ''

    y = 0

    while y < len(words[0]):
        x = 0

        while x < len(words):
            print(words[x][y])
            x += 1
        

        y += 1

# runtime ??
# runspace ??

# validWordSquare([
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]) #true

# validWordSquare([
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]) #true

validWordSquare([
  "ball",
  "area",
  "read",
  "lady"
]) #false bc row[3] != col[3] 

