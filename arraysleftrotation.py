"""
Hackerrank Interview Prep - Arrays

input: list of integers, int - how many to shift over
output: list of shifted integers
"""

def rotate_left(nums, shift):
	shifted = []

	for num, idx in enumerate(nums):
		print('idx', idx)
		print('num', num)

nums = [1, 2, 3, 4, 5]
shift = 4
# expect: 5 1 2 3 4
print(rotate_left(nums, shift))