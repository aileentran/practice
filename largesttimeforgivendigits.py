"""
Leetcode challenge - first week of September 2020

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

"""
# thoughts
# input: list of nums
# output: string -> "hh:mm"
# h1 <= 2 max nums in this range is 4; min 1
# h2 <= 4 max is 3; min 1
# m1 <= 5 max is 2
# m2 <= 9 max is 1

def largest_time_from_digits(nums):
	# counters for hh:mm
	h1 = h2 = m1 = m2 = 0

	for num in nums:
		if num <= 2:
			h1 += 1

		if 

	
"""
Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""

"""
nums = [1,2,3,4]
# nums = [5,5,5,5]

print(largest_time_from_digits(nums))