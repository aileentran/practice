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
# thoughts
# make a dictionary with letters as keys with  1 - 26 as values
# ohh! maybe just a loop? bc.. I'm lazy.

# make result variable = 0
# then loop through the string of letters
# find the key and value
# summ it to the result variable

# return the result!

def excelnum(letters):
    col_value = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
    }
    # each letter has 26 options => kind of like decimal/hexidecimal etc.
    
    col = 26 ** (len(letters) - 1)
    print(col)
    # setting up col value for multiple letters
    if len(letters) > 1:

        i = 0

        while i < len(letters) - 1:

            col *= col_value[letters[i]]

            i += 1

    # adding the very last letter to col
    print('col', col)

    # for letter in letters:
    #     print('letter', letter)
    #     print(col_value[letter])
    #     col *= col_value[letter]



    col += col_value[letters[-1]]

    return col

# print(excelnum('A')) #1
# print(excelnum('AB')) #28
# print(excelnum('ZY')) #701
# print(excelnum('ZZ')) #702
print(excelnum('AAA')) #703