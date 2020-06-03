# input: string
# output: dictionary - words(key) and num occured(value)



def wordcloud(sentence):
    # lowercase everything first?
    sentence = sentence.lower()

    # take out stuff that's not alpha
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for char in sentence:
        if char not in alpha and char != ' ' and char != '-' and char != "'":
            sentence = sentence.replace(char, '')

    # split string
    sentence = sentence.split()

    # make cloud dictionary
    cloud = {}

    for word in sentence:
        if word not in cloud:
            cloud[word] = 1
        else:
            cloud[word] += 1

    return cloud

# sentence = 'After beating the eggs, Dana read the next step:'
# longer = 'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.'
# print(wordcloud(longer))