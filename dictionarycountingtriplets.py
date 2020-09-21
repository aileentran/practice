"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""
# second iteration trying to account for more than one num w/ muliples
# ex [1, 3, 9, 9, 27, 27, 27]

def countTriplets2(arr, r):
    nums = {}
    triplets = 0
    
    for num in arr:
        if num not in nums:
            nums[num] = 1
        else:
            nums[num] += 1
    print(nums)
    for num in nums:
        sum_nums = 1
        second = num * r
        third = second * r
        print('potential triplet', num, second, third)
        if second in nums and third in nums:
            print('triplet', num, second, third)
            sum_nums *= nums[num]
            sum_nums *= nums[second]
            sum_nums *= nums[third]
            # sum_nums = max(nums[num], nums[second], nums[third])
            triplets += sum_nums
            print('sum_nums', sum_nums)
            print('triplets', triplets)
    return triplets
# Tests failed
nums = []

for i in range(1, 101):
    nums.append(1)
print(countTriplets2(nums, 1)) #161700, getting 1000000
################################################################
# Notes and thoughts
# input: list of integers, int - common ratio
# output: number of triplets

# first iteration with only one num has multiple
# ex [1, 3, 9, 9, 27]
# Complete the countTriplets function below.
# def countTriplets1(arr, r):
#     nums = {}
#     triplets = 0

#     for num in arr:
#         if num not in nums:
#             nums[num] = 1
#         else:
#             nums[num] += 1
#     print(nums)
#     for num in nums:
#         sum_nums = 0
#         second = num * r
#         third = second * r
#         print('potential triplet', num, second, third)
#         if second in nums and third in nums:
#             print('triplet', num, second, third)
#             # sum_nums += nums[num]
#             # sum_nums += nums[second]
#             # sum_nums += nums[third]
#             sum_nums = max(nums[num], nums[second], nums[third])
#             triplets += sum_nums
#             print('sum_nums', sum_nums)
#             print('triplets', triplets)
#     return triplets