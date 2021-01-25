"""
Leetcode 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


"""

# thoughts
# input: list of nums, target num
# output: list w/[start idx, end idx] OR [-1, -1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = [-1, -1]
        
        for i, num in enumerate(nums):
            if num == target and idx[0] < 0:
                idx[0] = i
            elif num == target and idx[0] >= 0:
                idx[1] = i
        
        if idx[0] >= 0 and idx[1] == -1:
            idx[1] = idx[0]
            
        return idx