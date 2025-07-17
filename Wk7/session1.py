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
