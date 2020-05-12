"""
Prob: check if binary tree is a proper binary search tree
binary search tree = (1) left nodes < curr node; (2) right nodes > curr node

thoughts
thinking of doing... depth first search
overall, based on curr node
if left > curr OR right < curr = return false
else moving on to next node! 

sooo... can implement depth first search with a stack 
put the tree root in first. 

in loop
pop from the stack 
if left > curr  or right < curr = return false

else:
	append left node
	append right node

return true outside!
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

def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree
    nodes = []
    nodes.append(root)

    while len(nodes) > 0:
        node = nodes.pop()
        print('node', node.value)

        # if NOT a leaf
        if node.left and (node.left.value > node.value or node.left.value > root.value):
            return False
        
        elif node.right and (node.right.value < node.value or node.right.value < root.value):
            return False

        else:
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    return True

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)


"""
valid tree works

    while len(nodes) > 0:
        node = nodes.pop()
        print('node', node.value)

        # if NOT a leaf
        if node.left or node.right:
            print('left', node.left.value)
            print('right', node.right.value)

            if (node.left.value > node.value) or (node.right.value < node.value):
                return False
            else:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

"""
