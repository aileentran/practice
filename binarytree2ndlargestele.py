"""
thoughts:
depth first search and keep on going down right most branches/leaves
get the largest value

largest ele
second largest = None
empty stack 
add the root into the stack

loop to traverse tree
just go down right side..? 
once find leaf, set largest ele as the value of rightmost leaf
pop off the leaf 
return the parent!!

check the left value 
if second largest is none: left value = second largest
else: 
"""

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.leaf = BinaryTreeNode(value)
        return self.left 

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

