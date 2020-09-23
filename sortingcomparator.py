"""
Hackerrank Interview Prep - Sorting
"""
# Notes
# comparator function returns -1, 0, 1
# for ascending (or alphabetical order): a < b = -1, a == b = 0, a > b = -1
# returns a, b, c
# so.. for descending: a > b = -1, a == b = 0, a < b = 1
# returns c, b, a

# info on comparators
# https://docs.oracle.com/javase/7/docs/api/java/util/Comparator.html#compare(T,%20T)
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return str(self.name) + " "  + str(self.score)
    def comparator(a, b):
        #same name and same score
        if a == b:
            return 0

        # same score but different names
        if a.score == b.score:
            #names are in ascending/alpha order!
            if a.name < b.name: 
                return -1
            else:
                return 1

        # different names, different scores
        if a.score > b.score:
            return -1

        if a.score < b.score:
            return 1

#####################################################
# first attempt and 4/8 right
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __repr__(self):
        return str(self.name) + " "  + str(self.score)
    
    def comparator(a, b):
        # yeesh! everything is the opposite since returning scores in descending order
        if a.score < b.score:
            return 1
        if a.score == b.score:
            # print('a', a.name)
            # print('b', b.name)
            # since scores are in descending order, we have to go backwards for alphabetized names = in order
            if b.name > a.name:
                # since the scores are the same, can just swap names!
                b.name, a.name = a.name, b.name
                # print('a', a.name)
                # print('b', b.name)
            return 0
        if a.score > b.score:
            return -1