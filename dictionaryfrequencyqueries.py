"""
Hackerrank Interview Prep - Dictionaries/Hash Maps
"""

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
# return 1 if true, 0 if false
# Complete the freqQuery function below.
def freqQuery(queries):
    nums_list = []
    nums_dict = {}

    for query in queries:
        print(query)
        op, num = query
        # print('op', op)
        # print('num', num)
        if op == 1:
            nums_list.append(num)
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        if op == 2:
            if num in nums_dict:
                idx = nums_list.index(num)
                nums_list.pop(idx)

                nums_dict[num] -= 1
                if nums_dict[num] <= 0:
                    nums_dict.pop(num)
        
        if op == 3:
            for num_key in nums_dict:
                if nums_dict[num_key] == num:
                    return 1
                else:
                    return 0

        print(nums_list)
        print(nums_dict)

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
]
print(freqQuery(q1))