"""
Leetcode - 238. Product of Array Except Self

input: list of nums
output: list of nums - product of all other eles except @ that index
"""

def productExceptSelf(nums):
    result = [1] * len(nums)
    for n, num in enumerate(nums):
        for r in range(len(result)):
            if n != r:
                result[r] *= num
    return result

nums = [1,2,3,4]
# [24,12,8,6]

print(productExceptSelf(nums))
