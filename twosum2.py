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
    idxs = []

    for i in range(len(nums) - 1):
        num1 = nums[i]
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            if num1 + num2 == target:
                return [i, j]

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
