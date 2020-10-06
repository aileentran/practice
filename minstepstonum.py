"""
Leetcode: Min Steps to Generate Number
Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3) --> // 3 for python
Find the minimum number of steps required to generate n from 1.
"""
# Notes and thoughts
# input: number - what w'ere trying to get to
# output: number - min number of steps to generate input num
# have a seen list
# start w/ 1, *= 2 until past goal number AND if //= 3 already in seen
# // 3 until we get to number 
def min_steps(num):

# Tests
num1 = 10 #expected: 6
num2 = 3 #expected: 7

print(min_steps(3))