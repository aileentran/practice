"""
Grokking Ch. 4

4.3 Find the maximum number in list
input: list of nums
output: num, the largest num in the list

Thoughts
base case: list is empty, return 0

return max(first int, func(rest of list))
"""

def maximum(nums):
    if nums == []:
        return None
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], maximum(nums[1:]))

nums1 = [9, 3, 8, 4, -1] #9
nums2 = [] #None
nums3 =[7] #7

print(maximum(nums1))
print(maximum(nums2))
print(maximum(nums3))
