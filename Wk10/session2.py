# problem 1

# PLAN
# Run a dfs
# visted set to prevent infinite calls
# global total variable
# each dfs
from collections import deque
def calculate_cost(flights, start, dest):
    q = deque([(start, 0)])
    visited = set([start])
    while q:
        for _ in range(len(q)):
            curr, amount = q.popleft()
            for location, cost in flights[curr]:
                if location == dest:
                    return amount + cost
                if location not in visited:
                    visited.add(location)
                    q.append((location, amount + cost))

    return -1
            
flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))

# Problem 2
# PLAN
# Set, to_visit and not_visted
# set for cycle
# for loop to iterate over the dictionary
#   check if the airport is in the set
#   no of flight += 1
#   run dfs

# dfs
# check if in cycle
# add the airport to the set
# traverse the children
def min_flights_to_expand(flights):
    visited = set()
    no_of_groups = 0
    
    def dfs(aip):
        if aip in visited:
            return
        visited.add(aip)
        for neighbour in flights[aip]:
            if neighbour not in visited:
                dfs(neighbour)
    
        
    for airport in flights:
        if airport not in visited:
            no_of_groups += 1
            dfs(airport)
            visited.add(airport)
    return no_of_groups - 1

flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))


# problem 3
# PLAN
# output array
# visited set
# create dfs funct
    # return if node in visited
    #   append child
    # or if node is dest return
    # for loop for children
    #   run dfs on children
# return output
def get_itinerary(flights, source, dest):
    visited = set()
    path = []

    def dfs(start):
        if start == dest:
            path.append(start)
            return True
        if start in visited:
            return False
        visited.add(start)
        path.append(start)
        for neighbour in flights[start]:
            if dfs(neighbour):
                return True
        path.pop()
        return False
    found = dfs(source)
    return path if found else None
flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))