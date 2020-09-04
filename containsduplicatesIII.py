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
    if len(nums) < 2:
        return False

    # in case k is > index of nums
    k = min(k, len(nums) - 1)

    i = 0

    while i <= i + k - 1:
        num_i = nums[i]
        
        j = i + 1

        while j <= i + k:
            num_j = nums[j]
            print('num_i', num_i)
            print('num_j', num_j)

            diff_t = abs(num_i - num_j)

            print('diff_t', diff_t)
            if diff_t <= t:
                return True

            j += 1
        print('\n')

        i += 1

    return False


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

# nums = [1,2,3,1]
# k = 3
# t = 0

# nums = [1,0,1,1]
# k = 1
# t = 2

# nums = [1,5,9,1,5,9]
# k = 2
# t = 3

# nums = [-3,3]
# k = 2
# t = 4
# output: ?; error = index of j out of range

# nums = [2,2]
# k = 3
# t = 0
# output: True

# nums = [3,6,0,4]
# k = 2
# t = 2
# output: True

# nums = [3,6,0,2]
# k = 2
# t = 2
# output: True

nums = [1,5,9,1,5,9]
k = 2
t = 3
# runtime error! 

print(contains_nearby_almost_duplicates(nums, k, t))