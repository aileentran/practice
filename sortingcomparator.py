"""
Hackerrank Interview Prep - Sorting
"""

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