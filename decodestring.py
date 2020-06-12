# input: string
# output: string

# takes in nums and letters; nums = spaces to skip and get letter! 

def decode(s):
    """Decode a string."""
    d = ''
    ints = '0123456789'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 0

    while i < len(s):
        char = s[i]
        
        if char in alph:
            d += char

        elif char in ints:
            i += int(char)

        i += 1

    return d

decode("0h") #'h'
decode("2abh") #'h'
decode("0h1ae2bcy") #'hey'