# Problem 1
def count_layers(sandwich):
    #print(sandwich)
    if len(sandwich) == 1:
        return 1
    return 1 + count_layers(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))

# Problem 2
def reverse_orders(orders):
    if len(orders) == 1:
        return orders[0]
    return reverse_orders(orders[1:]) + " " + orders[0] 


print(reverse_orders(["Bagel", "Sandwich",  "Coffee"]))

# Problem 3  
def can_split_coffee(coffee, n):
    if len(coffee) == 1:
        if coffee[0] % n != 0:
            return False
        else:
            return True
    return coffee[0] % n == 0 and can_split_coffee(coffee[1:], n)

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
print(can_split_coffee([5, 12, 16], 4))
print(can_split_coffee([4, 12, 16], 4))

# Problem 4
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Recursive solution
def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_b:
        return sandwich_a
    if not sandwich_a:
        return sandwich_b
    temp1 = sandwich_a.next
    temp2 = sandwich_b.next
    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(temp1, temp2)
    return sandwich_a


sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))

#Iterative solution
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    # If either list is empty, return the other
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a

    # Start with the first node of sandwich_a
    head = sandwich_a
    
    # Loop through both lists until one is exhausted
    while sandwich_a and sandwich_b:
        # Store the next pointers
        next_a = sandwich_a.next
        next_b = sandwich_b.next
        
        # Merge sandwich_b after sandwich_a
        sandwich_a.next = sandwich_b
        
        # If there's more in sandwich_a, add it after sandwich_b
        if sandwich_a:
            sandwich_b.next = next_a
        
        # Move to the next nodes
        sandwich_a = next_a
        sandwich_b = next_b

    # Return the head of the new merged list
    return head

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))

# Problem 6
def evaluate_ternary_expression_iterative(expression):
    stack = []
    for char in reversed(expression):
        if stack and stack[-1] == "?":
            stack.pop()
            true_exp = stack.pop()
            stack.pop()
            false_exp = stack.pop()
            if char == "T":
                stack.append(true_exp)
            else:
                stack.append(false_exp)
        else:
            stack.append(char)
    return stack[0]



print(evaluate_ternary_expression_iterative("T?2:3"))
print(evaluate_ternary_expression_iterative("F?1:T?4:5"))
print(evaluate_ternary_expression_iterative("T?T?F:5:3"))

print("evaluate_ternary_expression_recursive")

def evaluate_ternary_expression_recursive(expression):
    def helper(i):
        # Base case: return a digit or boolean value if it's just that
        if i >= len(expression) or expression[i] not in 'TF?':
            return expression[i], i
        
        # Current character should be a condition (either 'T' or 'F')
        condition = expression[i]
        i += 2  # Skip over '?' after the condition
        
        # Recursively evaluate the true_expression
        true_result, i = helper(i)
        
        # Skip over the ':' separating true and false expressions
        i += 1
        
        # Recursively evaluate the false_expression
        false_result, i = helper(i)
        
        # Return the appropriate result based on the condition
        if condition == 'T':
            return true_result, i
        else:
            return false_result, i
    
    # Start the recursive evaluation from the first character
    result, _ = helper(0)
    return result
    
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))
print(evaluate_ternary_expression_iterative("T?2:3"))
print(evaluate_ternary_expression_iterative("F?1:T?4:5"))
print(evaluate_ternary_expression_iterative("T?T?F:5:3"))