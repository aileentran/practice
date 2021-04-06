"""
Leetcode - 1679. Max Number of K-Sum Pairs

input: list of nums, int k
output: num - number of pairs that sum to k

Note:
in one op, can pick two nums that sum to k
remove those nums from the list

Thoughts
initial loop creating a dictionary of nums(key) and idxs (values)

counter for operations
second loop - goes through nums list
k - nums in dictionary.
if in list, increment counter and remove both idxs from dictionary

outside loop, return counter
"""

def maxOperations(nums, k):
    dict = {}
    ops = 0

    for i, num in enumerate(nums):
        if dict.get(num):
            dict[num].append(i)
        else:
            dict[num] = [i]
    print(dict)

    for i, num in enumerate(nums):
        pair = k - num
        print('num', num)
        print('pair', pair)
        if pair == num and len(dict[pair]) < 2:
            continue
        if dict.get(pair):
            ops += 1
            dict[num].remove(i)
            dict[pair].pop()
            if dict.get(num) and len(dict[num]) < 1:
                dict.pop(num)
            if dict.get(pair) and len(dict[pair]) < 1:
                dict.pop(pair)
        print('dict', dict)
        print(ops)

    return ops

nums1 = [1,2,3,4]
k1 = 5
"""
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
"""

nums2 = [3,1,3,4,3]
k2 = 6
"""
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""

nums3 = [3,1,5,1,1,1,1,1,2,2,3,2,2]
k3 = 1

nums4 = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k4 = 2
# output: 2 --> [1, 1] [1, 1]

# print(maxOperations(nums1, k1))
# print(maxOperations(nums2, k2))
# print(maxOperations(nums3, k3))
print(maxOperations(nums4, k4))
