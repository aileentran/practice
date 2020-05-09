"""
Create a new MaxStack class w/ method get_max()
get_max() returns largest item in the stack WITHOUT removing item
stack only contains ints! 

"""
class MaxStack(object):

	def __init__(self):
		"""Initialize empty stack w/ dynamic array"""
		self.items = []

	def push(self, item):
		"""Adding items to the end of the stack"""
		self.items.append(item)

	def pop(self):
		"""Remove last item in stack!"""

		# if stack is empty
		if not self.items:
			return None

		return self.items.pop()

	def peek(self):
		"""Look at last item in stack"""

		# if stack is empty
		if not self.items:
			return None

		return self.items[-1]

	def get_max(self):
		"""Find maximum value in stack"""

		largest = self.items[0]

		for item in self.items:
			if item > largest:
				largest = item

		return largest


a = MaxStack()
a.push(1)
a.push(123)
print(a.items)



