# input: list of words/strings
# output: boolean - true if row[i] == col[i]; false otherwise

# Q's: would ever get anything besides strings? chars only?

def validWordSquare(words):
	"""Check if valid word square where row[i] == col[i]."""


validWordSquare([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]) #true

validWordSquare([
  "abcd",
  "bnrt",
  "crm",
  "dt"
]) #true

validWordSquare([
  "ball",
  "area",
  "read",
  "lady"
]) #false bc row[3] != col[3] 

