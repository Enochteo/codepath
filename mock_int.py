# dfs 
"""
- input - tree
- output - boolean

PLAN
- base case
- NULL NODE
- LEAF NODE


- recursive
- LEFT, RIGHT

"""
"""
"""
# Implementation

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_to_leaf_sum(root, target_sum):
    if not root:
        return False
    if not root.left and not root.right:
        return target_sum == root.val
    return root_to_leaf_sum(root.left, target_sum-root.val) or root_to_leaf_sum(root.right, target_sum-root.val)

    
node = TreeNode(1)
node2 =  TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node.left = node2
node2.right = node3
node3.left = node4
node3.right = node5

root = TreeNode(1)
root2 =  TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)

root.left = node2
root2.right = node3
root3.left = node4
root3.right = node5
print(root_to_leaf_sum(node, 22))