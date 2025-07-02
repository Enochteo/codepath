class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    occurences = {}
    current = head
    total = 0
    while current:
        if current not in occurences:
            occurences[current.fish_name] = 1
        else:
            occurences[current.fish_name] += 1
        total += 1
        current = current.next
    return (round((occurences.get(fish_name, 0.0)/total), 2))
    #return round(occurences[fish_name]/total, 2) if fish_name in occurences else 0


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))