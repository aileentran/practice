"""
Leetcode - 1. Two Sum

input: list of nums, num - target
output: list of 2 nums - nums that sum to target

Notes:
has exactly 1 solution
cannot use the same num twice
return in any order
"""

def twoSum(nums, target):
    # creating dictionary to keep track of nums and their idxs
    nums_i = {}
    result = []

    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in nums_i:
            return [nums_i[num2], i]
        # vals can just be an int
        # bc line 20 will find duplicate complements early
        nums_i[num] = i

nums1 = [2,7,11,15]
target1 = 9
#Because nums[0] + nums[1] == 9, we return [0, 1].

nums2 = [3,2,4]
target2 = 6
#[1,2]

nums3 = [3,3]
target3 = 6
# [0,1]

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))
