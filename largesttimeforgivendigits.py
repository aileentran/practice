"""
Leetcode challenge - first week of September 2020

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

"""

def largest_time_from_digits(nums):


"""
Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""

"""
# nums = [1,2,3,4]
# nums = [5,5,5,5]

print(largest_time_from_digits(nums))