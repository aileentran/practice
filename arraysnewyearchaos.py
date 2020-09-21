"""
Hackerrank Interview Prep - Arrays
# Note: wants us to print the results instead of directly return it?
"""
# recent attempt
# Notes
# input: q -> list of nums from 1 - len(q)
# output: int - minimum number of bribes or "Too chaotic"
# total_bribes ~ each person can swap up 2 times and that's it!
# goal: get the line back in order and count the swaps

# empty bribes counter 
# have an array to keep track of idxs and where the people actually ar
# array idx = people - 1; array value = idx of where person is
# maybe..
# or dictionary for a bribe counter. key = person, value is swaps

# have an infinite loop
# maybe inner counter here..? if bribes >= 2, return "Too chaotic"
# if the person is > idx + 1, swap with the person behind it

# Complete the minimumBribes function below.
def minimumBribes2(q):
    total_bribes = 0
    bribe_counter = {}
    in_order = []
    
    for num in range(1, len(q) + 1):
        in_order.append(num)

    for person in q:
        bribe_counter[person] = 0

    while True:
        print(q)
        for person in bribe_counter: #try to remove loop
            if bribe_counter[person] > 2:
                return "Too chaotic"
        
        if q == in_order:
            return total_bribes
        
        for idx, person in enumerate(q):
            print(idx, q)
            if person > idx + 1:
                q[idx], q[idx + 1] = q[idx + 1], q[idx]
                bribe_counter[person] += 1
                total_bribes += 1
    
        
        print(bribe_counter)
        print(total_bribes)
        
    return total_bribes

# tests
q1 = [2, 1, 5, 3, 4] #3
q2 = [2, 5, 1, 3, 4] #Too chaotic
q3 = [5, 1, 2, 3, 7, 8, 6, 4] #Too chaotic
q4 = [1, 2, 5, 3, 7, 8, 6, 4] #7 

# print(minimum_bribes(q4))
print(minimumBribes2(q4))


############################################################
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
        
        if num != idx + 1:
            difference = abs(num - (idx + 1))   
        
        if difference > 2:
            return "Too chaotic"
        
        all_swaps += difference

    actual_swaps = all_swaps // 2
    return actual_swaps

# attempts 2: minimum swaps 2 idea?
# take in the mixed up queue
# recreate the ordered thingy with 2 swaps or lessss
# if a number bribes more than 2 spaces in one go, return "Too chaotic"

# counter = 0
# list: idx (val of queue - 1) and the value (idx is in queue)
# OR JUST MAKE A DICTIONARY @.@""
# key = item in list, value: idx of where it is at!

# loop through the queue and make the list of idxs to keep track

# empty bribes counter

# then loop through the queue
# if the bribes counter is > 2, return "too chaotic"
# if it's not the "right" 
# find the idx of where the thing actually is
# increment it closer to the actual location by 1
# adjust the list of idxs to match
# bribes += 1

# def minimum_bribes2(q):
#     bribes = 0
#     current_locations = {}

#     for idx, person in enumerate(q):
#         if person not in current_locations:
#             current_locations[person] = idx

#     for idx, person in enumerate(q):
#         if bribes > 2:
#             return "Too chaotic"

###################################################
# first solution from awhile ago
def minimumBribes(q):
    swaps = 0
    places = {} 

    # counter for how many individuals swapped in line
    for num in q:
        places[num] = 0

    print('original q', q)

    # runs until list is in order or more than 2 swaps
    while True:
        for num in q:
            if places[num] > 2: 
                print("Too chaotic")
                return

        # when q is finally in order
        if q == list(range(1, len(q) + 1)):
            print(swaps)
            return
        
        i = 0

        while i < len(q) - 1:
            # if current num is bigger than the next num
            if q[i] > q[i + 1]:
                places[q[i]] += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                swaps += 1

            i += 1


