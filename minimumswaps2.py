"""
Hackerrank Interview Prep - Arrays
"""

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