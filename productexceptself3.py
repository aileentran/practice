"""
Leetcode - 238. Product of Array Except Self

input: list of nums
output: list of nums - product of all other eles except @ that index

Thoughts - solving w/ 1 result array = O(1) time
make an empty result array
set right variable to keep track of products
loop using forward range
append left * right into results
"""

def productExceptSelf(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]


    right = 1
    for i in reversed(range(len(nums))):
        res[i] = res[i] * right
        right *= nums[i]

    return res

nums = [1,2,3,4]
# [24,12,8,6]

print(productExceptSelf(nums))
