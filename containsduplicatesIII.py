"""
Leetcode challenge

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
"""

# Thoughts:

# input: list, k, t 
# k = abs(index i - index j)
# t = abs(num[i] - num[j])

# output: boolean - true if <= k and t, false otherwise

# loop through list of nums up to idx k inclusive(?)
# see if ANY differences <= t
# return true if hit one

# outside loop, return false

def contains_nearby_almost_duplicates(nums, k, t):

    diff_t = 0

    i = 0

    while i <= k:
        num = nums[i]
        print('num', num)
        print('i', i)
        i += 1


"""
Examples

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

# Tests

nums = [1,2,3,1], k = 3, t = 0
# nums = [1,0,1,1], k = 1, t = 2
# nums = [1,5,9,1,5,9], k = 2, t = 3

print(contains_nearby_almost_duplicates(nums, k, t))