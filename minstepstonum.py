"""
Leetcode: Min Steps to Generate Number
Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3) --> // 3 for python
Find the minimum number of steps required to generate n from 1.
"""
# Notes and thoughts
# input: number - what we're trying to get to
# output: number - min number of OPERATIONS to generate input num FROM ONE
# have a seen list
# start w/ 1, *= 2 until past goal number AND if //= 3 already in seen
# // 3 until we get to number 
def min_steps(num_goal):
	ops = 0
	seen = [1]

	num = 1
	while num != num_goal:
		potential = num // 3
		if num < num_goal or (potential in seen):
			num *= 2
			seen.append(num)
			ops += 1
		else:
			num //= 3
			seen.append(num)
			ops += 1

	return ops
# run time: O(n^2)
# run space: O(s), ops is O(1); num O(1); O(s )

# Tests
num1 = 10 #expected: 6
num2 = 3 #expected: 7

print(min_steps(3))