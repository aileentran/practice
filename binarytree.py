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
			if value > current_node.value and current_node.right == None:
				current_node.right = Node(value)
				break
			
			if value < current_node.value and current_node.left == None:
				current_node.left = Node(value)
				break
			
			if value > current_node.value and current_node.right:
				current_node = current_node.right
			elif value < current_node.value and current_node.left:
				current_node = current_node.left

	def print_in_order(self, node):

		if node.left:
			self.print_in_order(node.left)

		print(node.value)

		if node.right:
			self.print_in_order(node.right)

	def delete_node(self, node, value):

		# base cases
		if value == node.value:
			print('curr', node.value)
			print('Deleting - root')
			# self.reconnect_tree(node)
			return 

		if value == node.left.value:
			print('curr', node.value)
			print('left node', node.left.value)
			print('Deleting - left')
			# self.reconnect_tree(node)
			return

		if value == node.right.value:
			print('curr', node.value)
			print('right node', node.right.value)
			print('Deleting - right')
			# self.reconnect_tree(node)
			return 

		# traversing tree
		print(value, 'not direct child of', node.value)
		if value < node.value:
			print('value', value)
			print('node.value', node.value)
			self.delete_node(node.left, value)

		if value > node.value:
			print('value', value)
			print('node.value', node.value)
			self.delete_node(node.right, value)

	def reconnect_tree(self, node):
		"""Helper function for delete_node to reconnect tree."""

			# if value == node.left.value:
			# 	print('Deleting', node.left.value)
			# 	if node.left.right:
			# 		node.left = node.left.right
			# 	elif node.left.left:
			# 		node.left = node.left.left
			# 	else:
			# 		node.left = None

			# if value == node.right.value:
			# 	print('Deleting', node.right.value)
			# 	node.right = node.right.right

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

# print(tiny_tree.print_in_order(root))

print(tiny_tree.delete_node(root, 4))
# consider what happens when deleting root :o 
# consider if value NOT in tree .-. 