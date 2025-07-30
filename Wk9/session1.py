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