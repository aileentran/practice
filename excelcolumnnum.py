"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

Ex:
A -> 1
B -> 2
...
AA -> 27
AB -> 28

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""

def excelnum(letters):


print(excelnum('A')) #1
print(excelnum('AB')) #28
print(excelnum('ZY')) #701