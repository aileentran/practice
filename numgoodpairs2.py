"""
Leetcode - 1512. Number of Good Pairs

input: list of nums
output: num - number of "good" Pairs

Notes:
good pair - num[i] == num[j] and i < j

Thoughts
approaching it using a dictionary
set an empty counter and empty dictionary

loop through input
if num not in dictionary, add it and set val to 1
if it is in dictionary, increment counter and increment val
"""
def numIdenticalPairs(nums):
    numbers = {}
    pairs = 0
    for num in nums:
        if num not in numbers:
            numbers[num] = 1
        else:
            pairs += numbers[num]
            numbers[num] += 1
    return pairs

nums1 = [1,2,3,1,1,3] #4
nums2 = [1,1,1,1] #6
nums3 = [1,2,3] #0

print(numIdenticalPairs(nums1))
print(numIdenticalPairs(nums2))
print(numIdenticalPairs(nums3))
