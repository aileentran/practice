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
		# check to see if value in tree
		if node.left == None or node.right == None:
			print(f'{value} does not exist in tree.')
			return False

		# base cases
		if value == node.value:
			self.reconnect_tree(node, node, 'root')
			return 

		if value == node.left.value:
			self.reconnect_tree(node, node.left, 'left')
			return

		if value == node.right.value:
			self.reconnect_tree(node, node.right, 'right')
			return 

		# traversing tree
		if value < node.value:
			self.delete_node(node.left, value)

		if value > node.value:
			self.delete_node(node.right, value)

	def reconnect_tree(self, curr_node, node_to_delete, left_or_right):
		"""Helper function for delete_node to reconnect tree - prioritizing connecting right (larger) values."""

		# TODO: reinsert left branch of deleted node into tree
		# more details in notebook
		if node_to_delete.right:
			if left_or_right == 'left':
				curr_node.left = node_to_delete.right
			else:
				curr_node.right = node_to_delete.right

			# checking if node_to_delete has a left node and attach to new node
			if node_to_delete.left:
				if left_or_right == 'left':
					curr_node.left.left = node_to_delete.left
				else:
					curr_node.right.left = node_to_delete.left
			return

		# node to delete does NOT have a right value
		if node_to_delete.left:
			if left_or_right == 'left':
				curr_node.left = node_to_delete.left
			else:
				curr_node.right = node_to_delete.left
			return

		# node_to_delete has no children
		if left_or_right == 'left':
			curr_node.left = None
		else:
			curr_node.right = None

tiny_tree = BinaryTree(5)
root = tiny_tree.root
# print(tiny_tree.print_root())
# print(root.parent)

tiny_tree.insert(9)
# print(root.right.value)
# print(root.right.parent.value)

tiny_tree.insert(3)
# print(root.left.value)
# print(root.left.parent.value)

tiny_tree.insert(2)
# print(root.left.left.value)

tiny_tree.insert(1)

tiny_tree.insert(7)

tiny_tree.insert(6)
# print(root.right.left.value)

tiny_tree.insert(4)
# print(root.left.right.value)

tiny_tree.insert(8)
tiny_tree.insert(12)
tiny_tree.insert(10)
tiny_tree.insert(13)
# print(root.right.right.value)

print(tiny_tree.delete_node(root, 9))

print(root.value)
print(root.right.value)

tiny_tree.print_in_order(root)


# consider what happens when deleting root :o 
# consider if value NOT in tree .-. 