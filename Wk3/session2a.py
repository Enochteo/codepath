# Problem 1
from collections import deque
def blueprint_approval(blueprints):
    blueprints.sort()
    queue = deque()
    for design in blueprints:
        queue.append(design)
    result = []
    while queue:
        result.append(queue.popleft())
    return result


print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 

# Problem 2
def build_skyscrapers(floors):
    stack = []
    skyscrapers = 0
    for floor in floors:
        if not stack or stack[-1] < floor:
            skyscrapers += 1
            stack = [floor]
        else:
            stack.append(floor)
    return skyscrapers

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

# Problem 3
def max_corridor_area(segments):
    l = 0
    r = len(segments)-1
    max_area = 0
    while l<=r:
        area = min(segments[l], segments[r]) * (r-l)
        if area > max_area:
            max_area = area
        if segments[l] <=segments[r]:
            l += 1
        else:
            r-=1
    return max_area
            

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 