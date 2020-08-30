class BinaryTree(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def print_tree(self):
		return self.value

	def insert_left(self, value):
		self.left = BinaryTree(value)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTree(value)
		return self.right

tiny_tree = BinaryTree('seedling')
print(tiny_tree.value)

tiny_tree.insert_left('left leaf')
print(tiny_tree.left.value)

tiny_tree.insert_right('right leaf')
print(tiny_tree.right.value)