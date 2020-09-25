"""Leetcode mock"""
# Notes
# input: sorted array, target value
# output: return idx of target, 
# if no target, return idx where it would be if it were inserted in order

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for num in nums:
            if num == target:
                return nums.index(target)
        
            if num > target:
                return nums.index(num)
        
#         target is NOT in list
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)