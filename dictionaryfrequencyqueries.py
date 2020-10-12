"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""
# Thoughts
# input: list of tuples (operation, data)
# input forms stuff we do to an array
# 1 = add data; 2 = delete 1 occurence of data
# 3 = check if any int occurs data times - 1 if yes, 0 if no
# output: 1 if yes, 0 if no

# make the actual list 
# if run into 3 operation, create dictionary counter - data(key): count(data)
# Complete the freqQuery function below.
def freqQuery(queries):
    nums = []
    count = {}
    for query in queries:
        op, data = query
        # print('op', op)
        # print('data', data)
        if op == 1:
            nums.append(data)
            if data not in count:
                count[data] = 1
            else:
                count[data] += 1
        
        if op == 2 and data in nums:
            nums.remove(data)
            if data in nums:
                count[data] -= 1
            else:
                count.pop(data)
        
        if op == 3:
            for idx, num in enumerate(count):
                if count[num] == data:
                    print(1)
                    break
                print('idx', idx)
                if idx == len(count.keys()) - 1 and count[num] != data:
                    print(0)


        # print(nums)
        # print(count)


# Tests
q1 = [
[1, 5],
[1, 6],
[3, 2],
[1, 10],
[1, 10],
[1, 6],
[2, 5],
[3, 2]
] # 0 1
q2 = [
[3, 4],
[2, 1003],
[1, 16],
[3, 1]
] # 0 1
q3 = [
[1, 3],
[2, 3],
[3, 2],
[1, 4],
[1, 5],
[1, 5],
[1, 4],
[3, 2],
[2, 4],
[3, 2]
] # 0 1 1
freqQuery(q3)












#############################################
# Notes
# input: a list of tuples *data structure working with is array!
# input (1, x) -> insert x in data structure
# input (2, y) -> delete 1 occurence of y
# input (3, z) -> check if any integer has exactly z frequency;
# output ONLY for (3, z): 1 if true, 0 if false
# 1 and 2 are just manipulations of the array 

# soo, make an empty array as the data structure 
# ^ maybe a dictionary counter is enough?
# make empty dictionary for a counter: inserted num (key), num of occurences (value)

# loop through the queries 2d queries
# (manipluation/query, num we're adding/removing/count)
# prob nested loop .-. 
# each row is a query, col 1 is the type, col 2 is the change
# if 1, append value to array and add to dictionary (or increase counter)
# if 2, check if in dictionary, if not move on, if it is, reduce by 1 and remove from array
# if 3, look to see if in dictionary and if count matches value
# PRINT 1 if true, 0 if false
# Complete the freqQuery function below.
def freqQuery1(queries):
    # nums_list = []
    nums_dict = {}

    for query in queries:
        # print('query', query)
        op, num = query

        if op == 1:
            # nums_list.append(num)
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        if op == 2:
            if num in nums_dict:
                # idx = nums_list.index(num)
                # nums_list.pop(idx)

                nums_dict[num] -= 1
            
                if nums_dict[num] <= 0:
                        nums_dict.pop(num)
        
        if op == 3:
            values = list(nums_dict.values())   
            if num in values:
                print(1)
            else:
                print(0)

        # print(nums_list)
        # print(nums_dict)

