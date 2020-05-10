"""
Create a new MaxStack class w/ method get_max()
get_max() returns largest item in the stack WITHOUT removing item
stack only contains ints! 

"""
class Stack(object):
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

class MaxStack(object):

	def __init__(self):
		self.stack = Stack()
		self.max_stack = Stack()

	def push(self, item):
		self.stack.push(item)

		if self.max_stack.peek() is None or self.max_stack.peek() < item:
			self.max_stack.push(item)

	def pop(self):
		if len(self.stack) == 0:
			raise ValueError('The stack is empty! There is nothing to remove')

		popped = self.stack.pop()

		if popped == self.max_stack.peek():
			self.max_stack.pop()

	def get_max(self):
		"""Find maximum value in stack"""
		return self.max_stack.peek()


a = MaxStack()
a.push(1)
a.push(123)
print(a.max_stack.items)