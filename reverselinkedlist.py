"""
input: head of a list
output: NEW head of a list

access tooo:
node.value
node.next
node.next.next..?

there's probably a recursive way to do this... buut
maybe something about two pointers? or three..? 

"""

class LinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.next = None

a = LinkedListNode('a')
b = LinkedListNode('b')
c = LinkedListNode('c')
d = LinkedListNode('d')

# no cycle
a.next = b
b.next = c
c.next = d

def reverse(head_of_list):
	
	curr = head_of_list
	prev = None
	nex = None
	
	while curr:
		nex = curr.next
		curr.next = prev

		prev = curr
		curr = nex

	return prev
		