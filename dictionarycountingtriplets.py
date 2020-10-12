"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""
# Notes 
# input: array of ints, ratio to *= 
# output: int - number of triplets

# dictionary of potential triplets - num(key): [i, j ,k] (value)
# dictionary counting the nums that pop up
# errmm.. something about ADDING associated counter nums
# Complete the countTriplets function below.
def countTriplets(arr, r):
    total = 0
    triplets = {}
    count  = {}
    for num in arr:
        sec = num * r
        third = num * r * r
        if sec in arr and third in arr:
            triplets[num] = [num, sec, third]
        
        if num not in count.keys():
            count[num] = 1
        else:
            count[num] += 1
        # print(num)
        # print(triplets)
        # print(count)
    print(triplets)
    print(count)
    # if len(triplets.keys()) > 0:
    #     total = 1
    
    for triplet in triplets.values():
        num1, num2, num3 = triplet
        
        # total *= count[num1]
        # total *= count[num2]
        # total *= count[num3]
        if count[num1] > 1:
            total += count[num1]
        if count[num2] > 1:
            total += count[num2]
        if count[num3] > 1:
            total += count[num3]
        print(triplet)
        print('num1', count[num1])
        print('num2', count[num2])
        print('num3', count[num3])
        print(total)
    
    return total

# Tests failed
nums = []

for i in range(1, 101):
    nums.append(1)

# 100000 1
# 1 100 10000 100000 1000000 1000000000 1000000000 10000000 100000 100000000 1000 100000000 1000 1000 10000000 10000 100 1000 1 100 100000 1 10000 1000000 100 1000 100 1000000 100000 100000 10000 100 10000000 100000000 10000000 10000 1 100000000 1000 100000 1000000 10000000 100000 100 1 100 1000000 100 10000000 1000000 1000000 100 100000000 10 10 1000 1000000 1000 1000000000 10 1 1000 100000 1 1000 1000 10000 100000 10 1000000000 10 1 1000000 1000000 100 100000000 1000000000 1 10 100000000 1000000 10000000 1000 10000 1 10000 1000000000 1000000 1000000000 100000000 1000000000 1000000000 1000 100000 1000000000 1000000000 1 100000 10000 10 100000 100000 10 1000 10000 100000 100 100000 100000 1000 1000 10 100 1000000 100000000 100000 100 10000000 1000 10 100000000 100000 10 1000 100 1 100 100 100000000 10000000 1000 1000 10000 10000000 1000000 100000000 100 1 1000 100000000 1000 1000000000 10 100000000 10000000 10 100000 1 10 100000000 10 1000000000 100000 100 100 10000000 100000 10000000 1000000000 1000, etc.

# expected output: 1667018988625
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