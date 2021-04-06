"""
Leetcode - 1679. Max Number of K-Sum Pairs

input: list of nums, int k
output: num - number of pairs that sum to k

Note:
in one op, can pick two nums that sum to k
remove those nums from the list
"""

def maxOperations(nums, k):
    return

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

print(maxOperations(nums1, k1))
print(maxOperations(nums2, k2))
