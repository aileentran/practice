

def rev(s):
    """Reverse word-order in string, preserving spaces."""
    if len(s) < 0:
    	return s

    words = s.split(' ')
    rev_words = []

    i = len(words) - 1

    while i >= 0:
    	word = words[i]
    	rev_words.append(word)
    	i -= 1

    return (' '.join(rev_words))


# tests
print(rev("")) # ''
print(rev("hello")) # 'hello'
print(rev("hello world")) # 'world hello'
print(rev(" hello  world   ")) # '   world  hello '