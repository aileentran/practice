"""
Hackerrank Interview Prep - Arrays
"""
# Notes
# input: unordered array of ints from 1 - len(array)
# output: integer - minimum number of swaps to get it back in order

# empty swap counter
# an array to keep track of idxs of where the value is SUPPOSED to be
# loop through the array and make it 

# loop through the array
# if the current value NOT idx + 1, 
# find where it is in the current array and swap it
# update the tracker array
# anddd.. increase the swap counter 

# outside loop, return swap counter

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # idx = array value, value = idx of where it's at
    curr_idxs = [0] * len(arr) 
    swaps = 0

    for idx, num in enumerate(arr):
        curr_idxs[num - 1] = idx

    for idx, num in enumerate(arr):
        if num != idx + 1:
            curr_idx = curr_idxs[idx]
            # swap values
            arr[idx], arr[curr_idx] = idx + 1, arr[idx]
            # update curr_swaps
            curr_idxs[idx], curr_idxs[arr[curr_idx] - 1] = idx, curr_idx
            
            swaps += 1

    return swaps



################################################
# thoughts
# input = list of integers
# output = integer -> minimum number of swaps
# correct order - length of list in ascending = is idx + 1

# Complete the minimumSwaps function below.
def minimum_swaps(arr):
    counter = 0
    arr_idx_tracker = [0] * len(arr)

    for idx, val in enumerate(arr):
        arr_idx_tracker[val - 1] = idx

    for idx, num in enumerate(arr):
        # print('arr', arr)
        # print('arr_idx_tracker', arr_idx_tracker)
        if num != idx + 1:
            # print('val supposed to have', idx + 1)
            idx_of_correct_val = arr_idx_tracker[idx]
            # print('where it is', idx_of_correct_val)
        
            arr[idx], arr[idx_of_correct_val] = idx + 1, arr[idx]
            # print('swapped!', arr)

            # print('updating arr_idx_tracker. beep boop boop!')
            # print('idx', idx)
            # print('arr_idx_tracker[idx]', arr_idx_tracker[idx])

            # print('idx_of_correct_val', idx_of_correct_val)
            # print(arr[idx_of_correct_val])
            # print('arr_idx_tracker[arr[idx_of_correct_val] - 1]', arr_idx_tracker[arr[idx_of_correct_val] - 1])

            arr_idx_tracker[idx], arr_idx_tracker[arr[idx_of_correct_val] - 1] = idx, idx_of_correct_val

            # print('arr_idx_tracker', arr_idx_tracker)
            counter += 1

            # print('\n')

    return counter

# test cases!
arr1 = [4, 3, 1, 2] #3
arr2 = [2, 3, 4, 1, 5] #3
arr3 = [1, 3, 5, 2, 4, 6, 7] #3

print(minimum_swaps(arr1))