"""
Grokking ch. 4

4.1 Write recursive solution for summing nums
input: list of nums
output: num - sum of all nums in list

Thoughts
base case = empty list, return 0

return num (first int of list) + func(rest of list)
"""

def sum(nums):
    if nums == []:
        return 0
    return nums[0] + sum(nums[1:])

nums1 = [2, 4, 6] #12
nums2 = [] #0

print(sum(nums1))
print(sum(nums2))
