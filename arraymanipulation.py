"""
Hackerrank Interview Prep - Arrays
"""
# Notes
# input: n = length of list of 0s; queries = [[a, b, k]...[an, bn, kn]]
# output: integer -> largest num

# a = start integer (idx + 1)
# b = last int (idx + 1) inclusive
# k = num that you add to integers from a to b

# Thoughts
# make the list of 0s based on n
# empty max_num

# loop through the queries -> nested loop 
# q[row][abk]
# sum k from 0 list from a to b -> loop here? 
# as summing, keep track of largest num

# outside probably triple nested loop
# see if need to loop through list to find largest sum
# return largest sum

def arrayManipulation(n, queries):
    list_of_n = [0] * n
    max_sum = 0

    for q in queries:
        start, end, summand = q
        print('start', start)
        print('end', end)
        print('summand', summand)

        i = start - 1
        while i < end:
            list_of_n[i] += summand
            if list_of_n[i] > max_sum:
                max_sum = list_of_n[i]
            i += 1
        print(list_of_n)
    
    return max_sum

# Tests
n1 = 5
queries1 = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# output: 200

n2 = 10 
queries2 = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
# output: 10

n3 = 10
queries3 = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
# output: 31
