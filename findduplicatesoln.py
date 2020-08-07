"""
Analyzing potential solutions that takes: space O(1) & time O(n)

Original problem:
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

def printRepeating(arr, size): 
      
    print("The repeating elements are: ") 
      
    for i in range(0, size): 
          
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            print (abs(arr[i]), end = " ") 

arr = [1, 2, 3, 1, 3, 6, 6] 
arr_size = len(arr) 
  
printRepeating(arr, arr_size