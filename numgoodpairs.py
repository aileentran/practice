"""
Leetcode - 1512. Number of Good Pairs

input: list of nums
output: num - number of "good" Pairs

Notes:
good pair - num[i] == num[j] and i < j

Thoughts
set a counter to 0
nested loop through nums w/ inner
if num1 == num2, increment counter.
"""

def numIdenticalPairs(nums):
    counter = 0

    for i in range(len(nums) - 1):
        num1 = nums[i]
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            if num1 == num2:
                counter += 1

    return counter

nums1 = [1,2,3,1,1,3] #4
nums2 = [1,1,1,1] #6
nums3 = [1,2,3] #0

print(numIdenticalPairs(nums1))
print(numIdenticalPairs(nums2))
print(numIdenticalPairs(nums3))
