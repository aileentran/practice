"""
Leetcode - Two Sum

input: list of nums, target num
output: two idx of nums that sum to target
Notes: only one solution, cannot be the same num, can be in any order
"""

def two_sum(nums, target):
    idxs = []
    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums and nums.index(diff) != i:
            idxs.append(i)
            idxs.append(nums.index(diff))
            return idxs

nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6
nums4 = [-1,-2,-3,-4,-5]
target4 = -8

print(two_sum(nums1, target1)) #[0, 1]
print(two_sum(nums2, target2)) #[1, 2]
print(two_sum(nums3, target3)) #[0, 1]
print(two_sum(nums4, target4)) #[2, 4]
