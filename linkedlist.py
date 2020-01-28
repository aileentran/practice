# for linked lists, need a Node class AND linked list class

class Node(object):
	"""Nodes"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""Creating linked lists."""

	def __init__(self):
		self.head = None
		# can have tail
		# self.tail = None

	def print_list(self):

		current = self.head

		while current is not None:
			print(current.data)

			current = current.next

	def find_item(self, data):

		current = self.head

		while current is not None:
			if current.data == data:
				return True

			current = current.next

		return False

