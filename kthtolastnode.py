"""
input: kth int, head of linked list
output:node - kth to last node of linked list

thoughts
is this faster? dict method 
make a dictionary: idx(key) and node(value)
counter..? 

counter - k = key
dict[key] = node

return node..?

hmm.. counter vs idx vs k... 
5 - 2 = 3 
idx 3 is item 3 
k seems to be.. 


OR 
make a list 

k = neg idx
return list[-k]


TEST CASE:
# Returns the node with value "Devil's Food" (the 2nd to last node)

kth_to_last_node(2, a)

"""

class LinkedListNode(object):

	def __init__(self, value):
		self.value = value
		self.next = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


def kth_to_last_node(k, head):
	"""Return node kth from the end!"""
	if k < 1:
		raise ValueError('Cannot find less than 1st to last node!')

	node_list = []

	while head:
		node_list.append(head)
		head = head.next

	return node_list[-k]