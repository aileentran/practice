"""
Leetcode: Min Steps to Generate Number

Link: https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number

Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3) --> // 3 for python
Find the minimum number of steps required to generate n from 1.
"""

# Notes
# input: int - number we are trying to generate
# output: int - min number of operations 

# empty operator counter
# num_goal set to 1

# infinite loop
# we multiply until get to >= num goal, counter += 1
# if past, we divide until <= num goal, counter += 1
# once num_goal == input, return the counter and get out of loop

def min_steps(num):
	operations = 0
	num_goal = 1
	seen = set()
	seen.add(1)

	while True:
		if num_goal == num:
			return operations

		print(num_goal)
		if num_goal < num or ((num_goal // 3) in seen):
			print('* 2')
			num_goal *= 2
			seen.add(num_goal)
			operations += 1
		else:
			print('// 3')
			num_goal //= 3
			seen.add(num_goal)
			operations += 1
			

		print('num_goal', num_goal)
		print('seen', seen)
		print('ops', operations)
		print('\n')

# Tests
num1 = 10
num2 = 3

print(min_steps(1000))

