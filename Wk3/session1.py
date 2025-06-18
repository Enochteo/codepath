
def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    stack = []
    order = []
    for i in range(n + 1):
        stack.append(i + 1)
        if i == n or arrival_pattern[i] == 'I':
            while stack:
                order.append(stack.pop())
    return order



# base cases
print(arrange_guest_arrival_order("I")) # 1,2
print(arrange_guest_arrival_order("D")) # 2,1
print(arrange_guest_arrival_order("ID")) # 2,3,1/1,3,2
print(arrange_guest_arrival_order("DI")) # 312/213
# test cases from the program
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDII"))#32145

#Problem 2
from collections import deque
def reveal_attendee_list_in_order(a_list):
    a_list.sort()
    reveal = deque()
    for i in range(len(a_list)-1, -1, -1):
        if reveal:
            reveal.appendleft(reveal.pop())
        reveal.appendleft(a_list[i])
    return reveal
"""
    while len(a_list)>1:
        reveal.appendleft(a_list.pop())
        reveal.appendleft(reveal.pop())
    if a_list:
        reveal.appendleft(a_list.pop())
    return reveal"""

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  
print(reveal_attendee_list_in_order([1,2,3,4,5,6,7,8,9]))    

