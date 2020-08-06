"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

# thoughts
# input: list of nums
# output: list of duplicate nums

# sort the list 
# empty curr variable

# loop through list
# store first number as current
# continue
# by the second number, compare it to the first
# if different, pop off the curr from the list
# set current to the second number
# if it is the same, continue

# def findduplicate(nums):
#     nums.sort()
#     curr = nums[0]

#     print('nums', nums)
#     print('curr', curr)
#     print('\n')
#     i = 0

#     while i < len(nums):
#         num = nums[i]
#         print('curr', curr)
#         print('i', i)
#         print('num', num)

#         if curr != num:
#             nums.pop(i - 1)
#             curr = num

#             print('nums', nums)
#             print('curr', curr)
#             print('\n')
#             continue

#         print('\n')
#         i += 1

#     return nums
##############################
# thoughts
# make empty dictionary as a counter
# loop through and make a counter of the numbers 

# loop through the dictionary, if the counter is 2, append into list

# return list

def findduplicate(nums):
    nums.sort()
    nums_counter = {}
    duplicates = []

    for num in nums:
        if num not in nums_counter:
            nums_counter[num] = 1
        else:
            nums_counter[num] += 1

    for num in nums_counter:
        if nums_counter[num] > 1:
            duplicates.append(num)

    return duplicates
# space complexity: O(n) + O(d) -> O(n)
# nums_counter -> O(n)
# duplicates -> O(d)

# run space: O(n^2)
# two unnested loops -> O(n)
# secret inner loop first loop -> O(n^2)
print(findduplicate([4,3,2,7,8,2,3,1])) #[2, 3]