# Problem 
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

def find_max(head):
    if not head:
        return 0
    # initialize a max_node_val
    max_node_val = head.value
    # initialize a pointer
    current = head
    # go through the list
    while current:
        if current.value > max_node_val:
            max_node_val = current.value
        current = current.next
    #   update the max_node_val  if bigger is found
    return max_node_val
    # return max_node val

# Test cases
head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))


# Problem 2
def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next: 
        last = current
        current = current.next

    last.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))


#Problem 3
def delete_dupes(head):
    # Initialize current
    current = head
    prev = Node("temp")
    prev.next = current

    # Check current element with next element
    while current.next:
        # If duplicate - delete current element
        if(current.value == current.next.value):
            prev.next = current.next.next
            current = prev.next
        current = current.next
        prev = prev.next
    return head

# Test Cases
head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

# Problem 4

def has_cycle(head):
    if not head or not head.next:
        return False
    # init a fast pointer
    fast = head
    # init a slow pointer
    slow = head
    # while loop fast, fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow.value == fast.value:
            return True
    #   slow = fast
    #   break and return true
    return False
    # return false

# Test cases
peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))

def remove_nth_from_end(head, n):
    
    if not head.next:
        return None
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    current = head
    prev = Node(0)
    prev.next = current
    index = length - n
    while current and index:
        prev = current
        current = current.next
        index -= 1
    prev.next = current.next
    return head


head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))