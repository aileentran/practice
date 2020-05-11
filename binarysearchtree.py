"""
Prob: check if binary tree is a proper binary search tree
binary search tree = (1) left nodes < curr node; (2) right nodes > curr node
"""

class BinaryTreeNode(object):

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert_left(self, value):
		self.left = BinaryTreeNode(value)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTreeNode(value)
		return self.right

