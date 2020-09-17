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

