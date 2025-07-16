'''
Poseidon, the ruler of Atlantis, has a map that shows various chambers hidden deep beneath the ocean. The map is currently stored as a nested list sections, with each section containing smaller subsections. Write a recursive function map_chambers() that converts the map into a nested dictionary, where each section and subsection is a key-value pair.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# '''
# # Problems 1
def map_chambers(sections):

    # base case: len(list) is 1
    if len(sections) == 1:
        return sections[0]

    return {sections[0] : {map_chambers(sections[1])}}

sections = ["Atlantis", ["Coral Cave", ["Pearl Chamber"]]]
print(map_chambers(sections))
# # Time comp. O(N)
# # Space comp. O(N)
# '''
# Expected output:
# {'Atlantis': {'Coral Cave': 'Pearl Chamber'}}
# '''


#Problem 2
'''
The people of Atlantis are collecting rare Trident Gems as they explore the ocean. The gems are arranged in a sequence of integers representing their value. Write a recursive function that returns the length of the consecutive sequence of gems where each subsequent value increases by exactly 1.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# '''

# def longest_trident_sequence(gems):
    
    
def recurse_longest_trident_sequence(gems, count, maximum):
    # check if we're not reaching the end of the list
    if len(gems) > 1:
        # There is a next element and its increase set count to count + 1 and adjust the maximum accordingly
        if gems[1] == gems[0] + 1:
            return recurse_longest_trident_sequence(gems[1:], count + 1, max(count + 1, maximum))
        # There is a next element and its decreasing set count to 0
        # if its not consecutive
        else:
            return recurse_longest_trident_sequence(gems[1:], 0, maximum)
    else:
        # Maximum
        return max(1 + count, maximum)
    
    return recurse_longest_trident_sequence(gems, 0, 0)


# print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
# print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))

# '''
# Example Output:

# 5
# Example 1 Explanation: longest sequence is 2, 3, 4, 5, 6

# 2
# Example 2 Explanation: longest sequence is 7, 8 or 1, 2
# '''


def longest_trident_sequence(gems):
    def helper(index, prev, count):
        if index == len(gems) or gems[index] < prev:
            return count
        return max(count, helper(index + 1, gems[index], count))
    helper(0, 0, 0)


'''
In Atlantis, buildings are arranged in concentric circles. The Greek gods have become unhappy with Atlantis, and have decided to punish the city by sending floods to sink certain buildings into the ocean.

Assume there are n buildings in a circle numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith building brings you the the (i+1)th building for 1 <= i < n, and moving clockwise from the nth building brings you to the 1st building.

The gods are sinking buildings as follows:

Start with the 1st building.
Count the next k buildings in the clockwise direction including the building you started at. The counting wraps around the circle and may count some buildings more than once.
The last building counted sinks and is removed from the circle.
If there is still more than one building standing in the circle, go back to step 2 starting from the building immediately clockwise of the building that was just sunk and repeat.
Otherwise, return the last building standing.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

''' 

def find_last_building(n, k):
    if n == 1:
        return 1
    return ((find_last_building(n-1, k) -1 + k) % n) + 1

print(find_last_building(5, 2))
print(find_last_building(6, 5))

'''
Example Output:

3
Example 1 Explanation: 
1) Start at building 1.
2) Count 2 buildings clockwise, which are buildings 1 and 2.
3) Building 2 sinks. Next start is building 3.
4) Count 2 buildings clockwise, which are buildings 3 and 4.
5) Building 4 sinks. Next start is building 5.
6) Count 2 buildings clockwise, which are buildings 5 and 1.
7) Building 1 sinks. Next start is building 3.
8) Count 2 buildings clockwise, which are buildings 3 and 5.
9) Building 5 sinks. Only building 3 is left, so they are the last building standing.

1
Example 2 Explanation: 
Buildings sink in this order: 5, 4, 6, 2, 3. The last building is building 1. 
'''

# Problem 4
class Node:
  def __init__(self, val, next=None):
      self.val = val
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):

    if not mission1:
        return mission2
    
    if not mission2:
        return mission1

    if mission1.val < mission2.val:
        mission1.next = merge_missions(mission1.next, mission2)
        left = True
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        left = False
    return mission1 if left else mission2
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))

# Problem 5
# Discussion

# Problem 6
def decode_scroll_recursive(scroll):
    def helper(index):
        res = ""
        while index < len(scroll):
            if scroll[index].isdigit():
                num = 0
                while index < len(scroll) and scroll[index].isdigit():
                    num = num * 10 + int(scroll[index])
                    index += 1
                index += 1
                mini_res, index = helper(index)
                res += mini_res * num
            elif scroll[index] == ']':
                return res, index + 1
            else:
                res += scroll[index]
                index += 1
        return res, index
    final_decoded_string, _ = helper(0)
    return final_decoded_string


scroll = "3[Coral2[Shell]]"
print(decode_scroll_recursive(scroll))

scroll = "2[Poseidon3[Sea]]"
print(decode_scroll_recursive(scroll))
