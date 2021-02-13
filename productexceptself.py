"""
Leetcode - 238. Product of Array Except Self

input: list of nums
output: list of nums, each ele product of array except self
"""

def productExceptSelf(nums):
    left = [0] * len(nums)
    right = [0] * len(nums)

    left[0] = 1
    for i in range(1, len(left)):
        left[i] = left[i - 1] * nums[i - 1]

    right[len(nums) - 1] = 1
    for i in reversed(range(len(right) - 1)):
        right[i] = right[i + 1] * nums[i + 1]
        # print('right[i + 1]', right[i + 1])
        # print('nums[i + 1]', nums[i + 1])

    result = []
    for i, num in enumerate(nums):
        result.append(left[i] * right[i])

    return result


nums = [1,2,3,4] #[24,12,8,6]

print(productExceptSelf(nums))
