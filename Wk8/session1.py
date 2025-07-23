# Problem 1 & 2
print("Problem 1")
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

# Problem 5
print("Problem 5")
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  if not root.left and not root.right:
      return root.val
  left_num = calculate_yield(root.left)
  right_num = calculate_yield(root.right)
  operand = root.val
  if operand == "+":
      return left_num + right_num
  elif operand == "-":
      return left_num - right_num
  else:
      return left_num * right_num
  
root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

# Problem 5
print("problem 5")

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_most_specific(taxonomy):
    specific = []
    def dfs(root, nodes):
        if not root:
            return
        if not root.left and not root.right:
            nodes.append(root.val)
        dfs(root.left, nodes)
        dfs(root.right, nodes)
    dfs(taxonomy, specific)
    return specific
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))

# Problem 5
print("problem 5")

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0
    if root.val > threshold:
        return 1 + count_old_growth(root.left, threshold) + count_old_growth(root.right, threshold)
    else:
        return 0 + count_old_growth(root.left, threshold) + count_old_growth(root.right, threshold) 
    

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))