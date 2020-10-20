"""
Leetcode: 910. Smallest Range II

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
"""

# thoughts
# input: list of ints, int k --> can be +k or -k added to each ele 
# creates new list of ints -> list b
# output: int - smallest difference between min and max values

# ohh.. maybe find the mean of the list
# if above the mean, subtract by k. if below the mean, add by k?
# find min and max of b
# find difference and return it :o 
# what to do if num == mean? :o 

def smallestRangeII(A, K):
    mean = 0
    sum_num = 0
    B = []
    
    for num in A:
        print('num', num)
        sum_num += num
   
    mean = sum_num / len(A)

    for num in A:
        if num > mean:
            b_num = num - K
            B.append(b_num)
        else:
            b_num = num + K
            B.append(b_num)
            
    min_num = min(B)
    max_num = max(B)
    
    return max_num - min_num

# Tests
A1 = [1]
K1 = 0 
# B = [1]; expected: 0

A2 = [0,10]
K2 = 2
# Output: 6
# Explanation: B = [2,8]

A3 = [1,3,6]
K3 = 3
# Output: 3
# Explanation: B = [4,6,3]

print(smallestRangeII(A1, K1))