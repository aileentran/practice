"""
Leetcode - 167. Two Sum II - Input array is sorted

input: sorted list of nums, target num
output: list of two nums - idxs that sum to target

Note
have exactly 1 solution and cannot reuse numbers
1 <= index <= length of list
"""
def twoSum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]

numbers1 = [2,7,11,15]
target1 = 9
# [1, 2] bc 2 + 7 = 9

numbers2 = [2,3,4]
target2 = 6
# [1, 3] bc 2 + 4 = 6

numbers3 = [-1,0]
target3 = -1
# [1, 2] bc -1 + 0 = -1

print(twoSum(numbers1, target1))
print(twoSum(numbers2, target2))
print(twoSum(numbers3, target3))
