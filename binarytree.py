# Binary search tree: add to left if greater than node, add to right if less than node
# functions to do: insert(node), delete(node), find_highest, find_lowest, print_in_order(),

class Node(object):
	def __init__(self, value):
		self.value = value
		self.parent = None
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
			if value > current_node.value and current_node.right == None:
				current_node.right = Node(value)
				current_node.right.parent = current_node
				break
			
			if value < current_node.value and current_node.left == None:
				current_node.left = Node(value)
				current_node.left.parent = current_node
				break
			
			if value > current_node.value and current_node.right != None:
				current_node = current_node.right
			elif value < current_node.value and current_node.left != None:
				current_node = current_node.left

	def print_in_order(self):
		current_node = self.root

		while current_node.left.value:
			print(current_node.value)

			current_node = current_node.left
			print(current_node.value)

tiny_tree = BinaryTree(5)
root = tiny_tree.root
# print(tiny_tree.print_root())
# print(root.parent)

tiny_tree.insert(7)
# print(root.right.value)
# print(root.right.parent.value)

tiny_tree.insert(3)
# print(root.left.value)
# print(root.left.parent.value)

tiny_tree.insert(1)
# print(root.left.left.value)

tiny_tree.insert(6)
# print(root.right.left.value)

tiny_tree.insert(4)
# print(root.left.right.value)

tiny_tree.insert(8)
# print(root.right.right.value)
