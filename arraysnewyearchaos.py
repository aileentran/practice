"""
Hackerrank Interview Prep - Arrays
"""
# thoughts
# input: list of integers
# output: integer -> minimum number of bribes to get to this point
# output: OR "Too chaotic"
# want to get the queue back in order!
# max num of bribes per person -> 2

# any of the ints moved MORE than 2 spots.. or 4..? -> fail early
# idx = val - 1
# a person can't be more than 2 ahead of it's i

# hmm.. have an empty counter 
# loop through the list 
# if the value is not in its right spot, add the difference into the counter
# if the difference is greater than 2 from its original spot, fail out and say it's too chaotic 

# outside of loop, return the counter

def minimum_bribes(q):
    all_swaps = 0 #double counted -> catching both ints that moved

    for idx, num in enumerate(q):
        difference = 0

        print('idx', idx)
        print('num', num)
        if num != idx + 1:
            difference = abs(num - (idx + 1))
            print('difference', difference)
        if difference > 2:
            return "Too chaotic"
        
        all_swaps += difference
        print('all_swaps', all_swaps)

    actual_swaps = all_swaps // 2
    # print('all_swaps', all_swaps)
    # print('actual_swaps', actual_swaps )
    return actual_swaps


# tests
q1 = [2, 1, 5, 3, 4] #3
q2 = [2, 5, 1, 3, 4] #Too chaotic
q3 = [5, 1, 2, 3, 7, 8, 6, 4] #Too chaotic
q4 = [1, 2, 5, 3, 7, 8, 6, 4] #7

print(minimum_bribes(q4))






















# first solution from awhile ago
def minimumBribes(q):
    swaps = 0
    places = {}

    for num in q:
        places[num] = 0

    while True:
        for num in q:
            if places[num] > 2: 
                print("Too chaotic")
                return

        if q == list(range(1, len(q) + 1)):
            print(swaps)
            return
        
        i = 0

        while i < len(q) - 1:
            if q[i] > q[i + 1]:
                places[q[i]] += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                swaps += 1

            i += 1