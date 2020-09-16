"""
Hackerrank Interview Prep - Arrays

input: list of integers, int - how many to shift over
output: list of shifted integers
"""

def rotate_left(nums, shift):
    shifted = [None] * len(nums)

    for idx, num in enumerate(nums):
        shifted[idx - shift] = num

    return shifted

nums = [1, 2, 3, 4, 5]
# shift = 4
# expect: 5 1 2 3 4

shift = 2
# expect: 3 4 5 1 2
print(rotate_left(nums, shift))