# input: takes in list of nums
# output: returns max in list

def maxnum(l):
	m = l[0]
	idx = 0

	for i, num in enumerate(l):
		if num > m:
			m = num
			idx = i

	return idx 

# run time: O(n)
# run space: O(2) --> O(1)

# input: list of nums
# output: return list of 5 * each num

def fivetimes(nums):
	five = []

	for num in nums:
		five.append(num * 5)

	return five

# run time: O(n)
# run space: O(n) 