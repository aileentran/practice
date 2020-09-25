"""
Leetcode: Min Steps to Generate Number

Link: https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number

Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3) --> // 3 for python
Find the minimum number of steps required to generate n from 1.
"""
# Notes
# input: int - goal number
# output: num - min number of steps to generate input from 1
# keep multiplying the number until it is greater than the goal and then divide by 3

# soo! have an empty counter
# number set to 1
# have a seen set to keep track of numbers we've visited

# make infinite loop 
# until number == goal, return the counter
# if the number <= goal or (num // 3) NOT in seen, multiply by 2 and add in seen and INCREMENT COUNTER
# else num // 3, increment counter

def min_steps2(goal):
	ops = 0
	num = 1
	seen = set()
	seen.add(num)

	while True:
		if num == goal:
			return ops

		print('num', num)
		if num < goal or (num // 3) in seen:
			num *= 2
		else:
			num //= 3

		ops += 1
		seen.add(num)















##########################################################
# Notes
# input: int - number we are trying to generate
# output: int - min number of operations 

# empty operator counter
# num_goal set to 1

# infinite loop
# we multiply until get to >= num goal, counter += 1
# if past, we divide until <= num goal, counter += 1
# once num_goal == input, return the counter and get out of loop

def min_steps1(num):
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

print(min_steps2(3))

