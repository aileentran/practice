"""
there's a list of integers 1 ... n but there are n + 1 items = duplicate somewhere

input: list of ints
output: int - le int that has duplicates 

soo! i gotta use a linked list to find the duplicate
node.value = the int 
node.next = the int's POSITION (idx + 1) in list

1. i gotta make the linkedlistnode class 
2. gotta turn list of ints into a linked list 
3. write the function to find the duplicate 

"""

class LinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.next = None

# def convert_to_ll(a_list):
# 	"""Convert a list into a linked list!"""
# 	head = None

# 	i = 0

# 	while i < len(a_list):
# 		print(i)
# 		if i == 0:
# 			head = LinkedListNode(a_list[i])
# 			head.next = head.value

# 			print('head val', head.value)
# 			print('head next', head.next)

# 		else:
# 			node = LinkedListNode(a_list[i])
# 			node.next = node.value
		
# 			print('node value', node.value)
# 			print('node next', node.next)

# 		i += 1

# 	return head

# print(convert_to_ll([1, 2, 3, 2]).next)

def find_duplicate(int_list):

	# for num in int_list:
	# 	print(num)
	# 	if int_list[num] != 'Boop!':
	# 		int_list[num] = 'Boop!'
	# 	else:
	# 		return num

	i = 0

	while i < len(int_list):
		pos = int_list[i]
		idx = pos - 1
		print(int_list)
		print('i', i)
		print('pos', pos)
		print('idx', idx)

		if int_list[idx] == '2 pointers':
			return pos
		elif isinstance(int_list[idx], int):
			int_list[idx] == '1 pointer'
		elif int_list[idx] == '1 pointer':
			int_list[idx] == '2 pointers'

		i += 1




