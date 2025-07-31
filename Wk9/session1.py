from collections import deque
class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
# # Problem 1
# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def listify_design(design):
#     # Level order traversal 

#     # Create a queue initially a list of the root
#     queue = deque()
#     queue.append(design)

#     # result list
#     result = []

#     # while loop - queue
#     while queue:
#         # create a level list
#         cur_level = []
#         # get length of queue
#         length = len(queue)
        
#         # do for lop
#         for i in range(length):
#         #   pop the queue from left
#             node = queue.popleft()

#         #   append its children
#             if node.left:
#                 queue.append(node.left)

#             if node.right:
#                 queue.append(node.right)

#         #   append the popped to the level
#             cur_level.append(node.val)

#         # append the level to the result
#         result.append(cur_level)
        
#     return result

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print(listify_design(croquembouche))

# # Time Complexity: O(n)
# # Space: O(n)
# def build_tree(values):
#   if not values:
#       return None

#   def get_key_value(item):
#       if isinstance(item, tuple):
#           return item[0], item[1]
#       else:
#           return None, item

#   key, value = get_key_value(values[0])
#   root = TreeNode(value, key)
#   queue = deque([root])
#   index = 1

#   while queue:
#       node = queue.popleft()
#       if index < len(values) and values[index] is not None:
#           left_key, left_value = get_key_value(values[index])
#           node.left = TreeNode(left_value, left_key)
#           queue.append(node.left)
#       index += 1
#       if index < len(values) and values[index] is not None:
#           right_key, right_value = get_key_value(values[index])
#           node.right = TreeNode(right_value, right_key)
#           queue.append(node.right)
#       index += 1

#   return root

# # Problem 2
# def zigzag_icing_order(cupcakes):
#       # Create a queue initially a list of the root
#     queue = deque()
#     queue.append(cupcakes)
#     reversed = False
#     # result list
#     result = []

#     while queue:
#         cur_lvl = deque()
#         for i in range(len(queue)):
#             node = queue.popleft()
#             cur_lvl.append(node.val)
#             if node.left:
#                 queue.append(node.left)

#             if node.right:
#                 queue.append(node.right)

#         if reversed:
#             while cur_lvl:
#                 result.append(cur_lvl.pop())
#         else:
#             while cur_lvl:
#                 result.append(cur_lvl.popleft())

#         reversed = not reversed
                
#     return result

# """
#             Chocolate
#            /         \
#         Vanilla       Lemon
#        /              /    \
#     Strawberry   Hazelnut   Red Velvet   
# """

# # Using build_tree() function included at top of page
# flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
# cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))

# # Problem 3
# def larger_order_tree(orders):
#     def inorder(node, sum_cum):
#         if not node:
#             return sum_cum
#         sum_cum = inorder(node.right, sum_cum)
#         node.val += sum_cum
#         sum_cum = node.val
#         return inorder(node.left, sum_cum)
#     inorder(orders, 0)
#     return orders
# order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# orders = build_tree(order_sizes)

# # using print_tree() function included at top of page
# print_tree(larger_order_tree(orders))

# Problem 4
class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def larger_order_tree(order_tree, order):
    if not order_tree:
        return order_tree
    q = deque([order_tree])
    while q:
        level_length = len(q)
        for i in range(level_length):
            node = q.popleft()
            if node == order:
                if i == level_length - 1:
                    return TreeNode(None)
                else:
                    return q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return TreeNode(None)
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
next_order3 = larger_order_tree(cupcakes, eclair)
next_order4 = larger_order_tree(cupcakes, cake)
print(next_order1.val)
print(next_order2.val)
print(next_order3.val)
print(next_order4.val)
    

class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def add_row(display, flavor, depth):
    if not display:
        return
    if depth == 1:
        temp = display
        display = TreeNode(flavor)
        display.left = temp
        return display
    q = deque([display])
    i = 0
    while q:
        i+=1
        for _ in range(len(q)):
            node = q.popleft()
            if i == depth - 1:
                left = node.left
                right = node.right
                node.left, node.right = TreeNode(flavor), TreeNode(flavor)
                node.left.left, node.right.right = left, right
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    return display


cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Red Velvet"]
display = build_tree(cupcake_flavors)

# Using print_tree() function included at top of page
print_tree(add_row(display, "Mocha", 3))