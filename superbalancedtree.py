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

def is_balanced(tree_root):

    # Determine if the tree is superbalanced

    # if tree has no nodes, it is superbalanced!
    if tree_root is None:
        return True

    depths = []

    # a stack of tuples: (node, depth)!
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes) > 0:
        # print('nodes', nodes)
        node, depth = nodes.pop()
        print('node', node.value)
        print('depth', depth)

        # at the leaves at bottom of tree!!
        if (not node.left) and (not node.right):
            print('At the leaves!')
            if depth not in depths:
                depths.append(depth)

            if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1] > 1)):
                return False
            print('depths', depths)
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True



