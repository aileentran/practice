# Binary search tree: add to left if greater than node, add to right if less than node
# functions to do: insert(node), delete(node), find_highest, find_lowest, print_in_order(),

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, value):
		self.root = Node(value)

	def print_root(self):
		return self.root.value

	def insert(self, value):

		current_node = self.root

		while True:
			if value > current_node.value and current_node.left == None:
				current_node.left = Node(value)
				break
			
			if value < current_node.value and current_node.right == None:
				current_node.right = Node(value)
				break
			
			if value > current_node.value and current_node.left != None:
				current_node = current_node.left
			elif value < current_node.value and current_node.right != None:
				current_node = current_node.right

tiny_tree = BinaryTree(5)
print(tiny_tree)
print(tiny_tree.root)

print(tiny_tree.print_root())