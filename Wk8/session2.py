from collections import deque 

# # Tree Node class
# class TreeNode:
#   def __init__(self, value, key=None, left=None, right=None):
#       self.key = key
#       self.value = value
#       self.left = left
#       self.right = right

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

        

# # Problem 1
# def sort_plants(collection):
#     sorted_plants = []
#     def dfs(col, sorted_plants):
#         if not col:
#             return
#         dfs(col.left, sorted_plants)
#         sorted_plants.append((col.key, col.value))
#         dfs(col.right, sorted_plants)
#     dfs(collection, sorted_plants)
#     return sorted_plants

# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
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
 
def find_flower(inventory, name):
    if not inventory:
        return False
    print(inventory.val)
    print(word_value(inventory.val), word_value(name))
    if word_value(inventory.val) == word_value(name):
        return True
    elif word_value(inventory.val) < word_value(name):
        return find_flower(inventory.right, name)
    else:
        return find_flower(inventory.left, name)

def word_value(word):
    total = 0
    for c in word:
        total += ord(c)  
    return total

values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 
# print(ord('Lilac') < ord('Lily'))