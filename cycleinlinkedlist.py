"""
input: first node in list
output: boolean - True if there is a cycle, false otherwise

nodes:
node.value
node.next

cycle = node.next points to a PREVIOUS node.value

thoughts:
have an array (or dict? maybe a little faster or a set!) of seen node values

loop through linked list 
if node.value in seen
return True
else:
	node.value added to seen 

outside loop
return false

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
d.next = b


def contain_cycle(node):
	seen = set()

	while node != None:
		print(seen)
		if node.value in seen:
			return True
		elif node.next == None:
			return False
		else:
			seen.add(node.value)	
			node = node.next
