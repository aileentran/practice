"""
Analyzing potential solutions that takes: space O(1) & time O(n)

Original problem:
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

"""
Solution 1: does NOT return anything.. need to return a list!

Approach:The elements in the array is from 0 to n-1 and all of them are positive. So to find out the duplicate elements, a HashMap is required, but the question is to solve the problem in constant space. There is a catch, the array is of length n and the elements are from 0 to n-1 (n elements). The array can be used as a HashMap.

Algorithm:
1) Traverse the array from start to end.
2) For every element,take its absolute value and if the abs(array[i])‘th element is positive, the element has not encountered before, else if negative the element has been encountered before print the absolute value of the current element.
"""

def printRepeating(arr, size): 
    print(arr)

    for i in range(0, size):
        num = arr[i]
        print('num', num)
        print('arr[abs(num)]', arr[abs(num)])
        if arr[abs(num)] >= 0: 
            arr[abs(num)] = -arr[abs(num)] 
            print('negative?', arr[abs(num)])
            print(arr)
            print('\n')
        else: 
            print('GOT A DUPLICATE!')
            print(abs(num)) 
            print('\n\n')

    return None

arr = [1, 2, 3, 1, 3, 6, 6] 
arr_size = len(arr) 
  
# printRepeating(arr, arr_size)


def find_duplicates(nums):

    for num in nums:

        if arr[abs(num)] >= 0: #haven't seen num yet
            arr[abs(num)] = -arr[abs(num)] #mark it by setting val to negative
        else: 
            print(abs(num) #have seen it! 

find_duplicates([1, 2, 3, 1, 3, 6, 6])
