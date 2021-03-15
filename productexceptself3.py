"""
Leetcode - 238. Product of Array Except Self

input: list of nums
output: list of nums - product of all other eles except @ that index

Thoughts - solving two arrays
create array for product of items "left" of current value
create array for product items "right" of current value - reverse direction

product of items = prev in "left/right" * curr's prev
left array starts w/1. right array ends with 1

loop through both arrays and multiply left * right
"""

def productExceptSelf(nums):
    left = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]
    # print(left)

    right = [1] * len(nums)
    for i in reversed(range(len(nums) - 1)):
        right[i] = right[i + 1] * nums[i + 1]
    # print(right)

    res = []
    for i in range(len(nums)):
        res.append(left[i] * right[i])

    return res

nums = [1,2,3,4]
# [24,12,8,6]

print(productExceptSelf(nums))
