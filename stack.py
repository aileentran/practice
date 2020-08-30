# Implementing stack w/list
# Last in, first out
# Functions: push, pop, peek

class Stack(object):
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

pancakes = Stack()
print(pancakes.items)

pancakes.push('blueberry')
pancakes.push('strawberry')
pancakes.push('matcha')
print(pancakes.items)

print(pancakes.pop())
print(pancakes.items)
print(pancakes.peek())