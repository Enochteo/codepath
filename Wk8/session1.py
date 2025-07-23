# Problem 1 & 2
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine_iterative(root):
    right_nodes = []
    while root:
        right_nodes.append(root.val)
        root = root.right
    return right_nodes

def right_vine_recursive(root):
    right_nodes = []
    def helper(root, right):
        if not root:
            return
        right.append(root.val)
        helper(root.right, right)
    helper(root, right_nodes)
    return right_nodes

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine_recursive(ivy1))
print(right_vine_recursive(ivy2))

print(right_vine_iterative(ivy1))
print(right_vine_iterative(ivy2))

#Problem 3
print("Problem 3")
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    node_list = []
    def postorder(root, nodes):
        if not root:
            return
        postorder(root.left, nodes)
        postorder(root.right, nodes)
        nodes.append(root.val)
    postorder(root, node_list)
    return node_list
magnolia = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")), TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

# Problem 4
print("Problem 4")
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    if not inventory:
        return 0
    return inventory.val + sum_inventory(inventory.left) + sum_inventory(inventory.right)

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))