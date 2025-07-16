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

def edit_dna_sequence(dna_strand, m, n):
    current = dna_strand
    while current:
        for _ in range(m-1):
            if current:
                current = current.next
        temp = current
        for _ in range(n+1):
            if current:
                current = current.next
        if temp:
            temp.next = current
    return dna_strand

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    slow = protein
    fast = protein
    res = set()
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow.value == fast.value:
            print(slow.value)
            break
    current = slow
    while current.value not in res:
        res.add(current.value)
        current = current.next
    return list(res)



protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



def split_protein_chain(protein, k):
    # find length of linked list
    # find the upper divisor length/k = number of node in segment - n
    # reset current to head
    # append the head
    # for loop n-1 times
    # temp = current
    # append current.next
    # current.next = none
    # append 
    pass