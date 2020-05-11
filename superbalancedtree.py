"""
Figure out if a tree is superbalanced!
superbalanced = diff of depths between any 2 leaf nodes <= 1

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

    