# Problem 1
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

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  
print(reveal_attendee_list_in_order([1,2,3,4,5,6,7,8,9]))    

# Problem 3
def arrange_attendees_by_priority(attendees, priority):
    less_thans = []
    equals = []
    greater_thans = []
    for num in attendees:
        if num < priority:
            less_thans.append(num)
        elif num == priority:
            equals.append(num)
        else:
            greater_thans.append(num)
    return less_thans + equals + greater_thans + ["brute"]

def arrange_attendees_by_priority1(attendees, priority):
    l = 0 # less thans
    r = len(attendees) - 1 # greater thans
    i = 0
    while i<=r:
        if attendees[i] < priority:
            attendees[l], attendees[i] = attendees[i], attendees[l]
            l += 1
            i += 1
        elif attendees[i] == priority:
            i += 1
        else:
            attendees[r], attendees[i] = attendees[i], attendees[r]
            r -= 1
    return attendees + ["two-pointer"]

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10))   
print(arrange_attendees_by_priority1([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 

