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
        self.left = BinaryTreeNode(value)
        return self.left 

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def find_second_largest(root_node):

    # Find the second largest item in the binary search tree
    # make tuple with node and value
    nodes = []
    nodes.append((root_node.value, root_node))

    for a_node in nodes:
        value, node = nodes[-1]

        if node.left:
            nodes.append((node.left.value, node.left))
        if node.right:
            nodes.append((node.right.value, node.right))

    nodes = sorted(nodes)

    return nodes[-2][0]

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)


        





