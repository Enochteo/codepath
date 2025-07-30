from collections import deque

# Problem 1
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    # Level order traversal 

    # Create a queue initially a list of the root
    queue = deque()
    queue.append(design)

    # result list
    result = []

    # while loop - queue
    while queue:
        # create a level list
        cur_level = []
        # get length of queue
        length = len(queue)
        
        # do for lop
        for i in range(length):
        #   pop the queue from left
            node = queue.popleft()

        #   append its children
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        #   append the popped to the level
            cur_level.append(node.val)

        # append the level to the result
        result.append(cur_level)
        
    return result

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))

# Time Complexity: O(n)
# Space: O(n)
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

# Problem 2
def zigzag_icing_order(cupcakes):
      # Create a queue initially a list of the root
    queue = deque()
    queue.append(cupcakes)
    reversed = False
    # result list
    result = []

    while queue:
        cur_lvl = deque()
        for i in range(len(queue)):
            node = queue.popleft()
            cur_lvl.append(node.val)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if reversed:
            while cur_lvl:
                result.append(cur_lvl.pop())
        else:
            while cur_lvl:
                result.append(cur_lvl.popleft())

        reversed = not reversed
                
    return result

"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))