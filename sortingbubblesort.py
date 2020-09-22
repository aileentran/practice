"""
Hackerrank Interview Prep - Sorting
"""
# Notes
# input: array of nums
# output: printing phrases w/number of swaps, first element, last element
# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    
    for i in range(len(a)): #follow each element in arr
        # print(i)
        for k in range(len(a) - 1): #move ele and swap
            # print('a[k]', a[k])
            # print('a[k + 1]', a[k + 1])
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                swaps += 1
                # print(a)
                # print(swaps)
    
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


########################################################
# Initial attempt
# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0

    for num in a:

        i = 0
        while i < len(a) - 1:

            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
            i += 1

    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')