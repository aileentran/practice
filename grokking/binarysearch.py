"""
Grokking Ch. 4

4.4 Binary search using recursion
input: list of nums, target num
output: true if in list, false otherwise

Thoughts
floor, ceil, and guess
guess = floor + half distance
base case: list is empty = return false
guess == target = return true

if guess < target
recursive case func([floor, guess])

if guess > target
recursive case func([guess, ceil])
"""

def binary(nums, target):
    return

nums1 = [1, 7, 4, 9, 10]
nums2 = [] #empty list
target1 = 4 #middle of list
target2 = 1 #beginning list
target3 = 10 #end of list
target4 = 12 #not in list

print(binary(nums1, target1)) # True
print(binary(nums2, target1)) # False
print(binary(nums1, target2)) # True
print(binary(nums1, target3)) # True
print(binary(nums1, target4)) # False
