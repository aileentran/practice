"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""
def countTriplets(arr, r):
    num_count = {} # count of num occuring in array
    in_a_triplet = {} # count how many times num is a part of triplet.. sort of?
    counter = 0

    print('num_count', num_count)
    print('in_a_triplet', in_a_triplet)
    for num in reversed(arr):
        next_num = num * r

        print('num', num)
        print('next_num', next_num)
        

        if next_num in in_a_triplet:
            counter += in_a_triplet[next_num]

        # counting potential triplets
        if next_num in num_count:
            if num not in in_a_triplet.keys():
                in_a_triplet[num] = num_count[next_num]
            else:
                in_a_triplet[num] += num_count[next_num]

        # counting occurence of num in arr
        if num not in num_count.keys():
            num_count[num] = 1
        else:
            num_count[num] += 1
        print('num_count', num_count)
        print('in_a_triplet', in_a_triplet)
        print('counter', counter)
        print('\n')

# Tests failed
# Test1
nums = []

for i in range(1, 101):
    nums.append(1)

# 100000 1
# 1 100 10000 100000 1000000 1000000000 1000000000 10000000 100000 100000000 1000 100000000 1000 1000 10000000 10000 100 1000 1 100 100000 1 10000 1000000 100 1000 100 1000000 100000 100000 10000 100 10000000 100000000 10000000 10000 1 100000000 1000 100000 1000000 10000000 100000 100 1 100 1000000 100 10000000 1000000 1000000 100 100000000 10 10 1000 1000000 1000 1000000000 10 1 1000 100000 1 1000 1000 10000 100000 10 1000000000 10 1 1000000 1000000 100 100000000 1000000000 1 10 100000000 1000000 10000000 1000 10000 1 10000 1000000000 1000000 1000000000 100000000 1000000000 1000000000 1000 100000 1000000000 1000000000 1 100000 10000 10 100000 100000 10 1000 10000 100000 100 100000 100000 1000 1000 10 100 1000000 100000000 100000 100 10000000 1000 10 100000000 100000 10 1000 100 1 100 100 100000000 10000000 1000 1000 10000 10000000 1000000 100000000 100 1 1000 100000000 1000 1000000000 10 100000000 10000000 10 100000 1 10 100000000 10 1000000000 100000 100 100 10000000 100000 10000000 1000000000 1000, etc.

# expected output: 1667018988625
# print(countTriplets(nums, 1)) #161700, getting 1000000

nums = [1, 3, 9, 9, 27, 81] 
r = 3
# expect 6
print(countTriplets(nums, r))
################################################
# Notes 
# input: array of ints, ratio to *= 
# output: int - number of triplets

# dictionary of potential triplets - num(key): [i, j ,k] (value)
# dictionary counting the nums that pop up
# errmm.. something about ADDING associated counter nums
# Complete the countTriplets function below.
def countTriplets2(arr, r):
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

################################################################
# Notes and thoughts
# input: list of integers, int - common ratio
# output: number of triplets

# first iteration with only one num has multiple
# ex [1, 3, 9, 9, 27]
# Complete the countTriplets function below.
def countTriplets1(arr, r):
    nums = {}
    triplets = 0

    for num in arr:
        if num not in nums:
            nums[num] = 1
        else:
            nums[num] += 1
    print(nums)
    for num in nums:
        sum_nums = 0
        second = num * r
        third = second * r
        print('potential triplet', num, second, third)
        if second in nums and third in nums:
            print('triplet', num, second, third)
            # sum_nums += nums[num]
            # sum_nums += nums[second]
            # sum_nums += nums[third]
            sum_nums = max(nums[num], nums[second], nums[third])
            triplets += sum_nums
            print('sum_nums', sum_nums)
            print('triplets', triplets)
    return triplets