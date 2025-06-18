# Problem 1
def total_treasure(treasure_map):
    total = 0
    for treasure in treasure_map.values():
        total += treasure
    return total
    


treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasure(treasure_map1)) 
print(total_treasure(treasure_map2)) 
from collections import Counter
def can_trust_message(message):
    return len(set(char for char in message.lower() if char.isalpha())) >= 26
def can_trust_messages(message):
    sentence_letters = set(message.lower())
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    return alphabets.issubset(sentence_letters)

message1 = "sphinx of bla135647847rgrsbjeck quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

print(can_trust_messages(message1))
print(can_trust_messages(message2))

def find_duplicate_chests(chests):
    seen = set()
    res = []
    for num in chests:
        if num in seen:
            res.append(num)
        seen.add(num)
    return res
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

def is_balanced(code):
    balanced_code = set(code)
    return len(code) - len(balanced_code) <= 1


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

# Problem 6
from collections import defaultdict
def find_treasure_indices(gold_amounts, target):
    visited = defaultdict()
    for i,v in enumerate(gold_amounts):
        remainder = target - gold_amounts[i]
        if remainder in visited:
            return [visited[remainder], i]
        visited[v] = i

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

# Problem 6
def organize_pirate_crew(group_sizes):
    result = {}
    for i, val in enumerate(group_sizes):
        if val not in result:
            result[val] = []
        result[val].append(i)
    #print(result)
    res = []


group_sizes1 = [3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 