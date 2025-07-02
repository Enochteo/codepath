class Villager:
    def __init__(self, name, species, personality,catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def add_item(self, item_name):
        valid_names = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu",  "cacao tree"}
        if item_name in valid_names:
            self.furniture.append(item_name)


def of_personality_type(townies, personality_type):
    
    res = []
    for t in townies:
        if t.personality == personality_type:
            res.append(t.name)

    return res

def message_received(start_villager, target_villager):
    current = start_villager
    while current is not None:
        if target_villager is not current:
            current = start_villager.neighbor
            start_villager = current
        else:
            return True
    return False

def message_received(start_villager, target_villager):
    current = start_villager
    while current:
        if current == target_villager:
            return True
        current = current.neighbor    
    return False    
"""
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")

isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider


print(message_received(isabelle, tom_nook))
print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))"""


# Problem 3
"""isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))"""

# Problem 1
"""apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)"""

# Problem 2
"""alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)"""

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

def catch_fish(head):
    
    if head:
        print(f'I caught a {head.fish_name}')
        return head.next
    else:
        print(f'Aw! Better luck next time!')


"""kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)"""

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))
