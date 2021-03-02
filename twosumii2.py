"""
Leetcode - 167. Two Sum II - Input array is sorted

input: list of nums, target num
output: two indices (or.. position rather = i + 1) that sum to target in a list

Notes:
exactly one solution
list of nums in ascending order
cannot use same element twice


Thoughts:
Have two pointers, one at the beginning and one at the end
hmm.. do i need to skip nums that are == to num before?
if the sum of two numbers is < target, move right pointer
if sum of two numbers > target, move left pointer
once two numbers == target, return list of indices
"""
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= len(numbers) and left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]


numbers1 = [2,7,11,15]
target1 = 9
# [1,2]

numbers2 = [2,3,4]
target2 = 6
# [1,3]

numbers3 = [-1,0]
target3 = -1
# [1, 2]

print(twoSum(numbers1, target1))
print(twoSum(numbers2, target2))
print(twoSum(numbers3, target3))
