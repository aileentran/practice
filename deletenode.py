class LinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.next = None

a = LinkedListNode('a')
b = LinkedListNode('b')
c = LinkedListNode('c')

a.next = b
b.next = c

"""
Create a function to delete one node in a singly linked list

input: node
output: return new linked list..? :o 

OHH!! take the next node and turn the current node to delete into those values!!

"""

def delete_node(node):
	next_node = node.next

	if next_node:
		node.value = next_node.value
		node.next = next_node.next
	else:
		raise Exception('Cannot delete the last node!')

	