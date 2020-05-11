"""
input: string
output: boolean: True if matching (), [], {}, false otherwise!

so ideasss!! 

have the thingy be a stack to store OPEN blah
have a dictionary to pair the open BLAH with associated closing thingy: closing(key), open[value]????

loop through the string 
if it's an open thingy, append into stack 
if it's a closing bracket 
if dict[closing] NOT equal stack[-1]
return false 
if dict[closing] == stack[-1]
then we pop that baby off 

outside loop
if the stack is empty, return true
else return false!

"""

def is_valid(code):

    # Determine if the input code is valid
    closing = {
    ')': '(',
    ']': '[',
    '}': '{'
    }

    opening = []

    for char in code:
        if char == '(' or char == '{' or char == '[':
            opening.append(char)
        elif char in closing:
            if len(opening) == 0 or closing[char] != opening[-1]:
                return False 
            else:
                opening.pop()

    if len(opening):
        return False

    return True





