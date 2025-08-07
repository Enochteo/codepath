# Problem I
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

def find_center(terminals):
    a, b = terminals[0]
    c, d = terminals[1]

    # The center must be the common node
    if a == c or a == d:
        return a
    else:
        return b
    """map = {}
    for ter in terminals:
        for t in ter:
            if t in map:
                map[t] += 1
            else:
                map[t] = 1
    for t, c in map.items():
        if c > 1:
            return t"""
terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

# Problem 3
# dfs
def get_all_destinations(flights, start):
    res = []
    visited = set()
    def dfs(state):
        for s in flights[state]:
            if s not in visited:
                visited.add(s)
                res.append(s)
                dfs(s)
    visited.add(start)
    dfs(start)
    return res


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
print(get_all_destinations(flights, "New York"))

# Problem 4
# DFS
from collections import deque
def get_all_destinations(flights, start):
    q = deque([start])
    res = []
    visited = set([start])
    while q:
        curr = q.popleft()
        if curr != start:
            res.append(curr)
        for s in flights[curr]:
            if s not in visited:
                visited.add(curr)
                q.append(s)
    return res
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"], 
    "New York": []  
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))

# Problem 5
def find_itinerary(boarding_passes):
    map = {}
    res = []
    arrivals = set() # store all arrivals coz start cannot be in attivals as there are no cycles
    for dest, arr in boarding_passes:
        map[dest] = arr
        arrivals.add(arr)
    for s in map:
        if s not in arrivals:
            start = s
    res.append(start)
    while start in map:
        start = map[start]
        res.append(start)
        
    return res

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))

# Problem 6 BFS
def find_itinerary(boarding_passes):
    map = {}
    arrs = set()
    for dept, arr in boarding_passes:
        map[dept] = arr
        arrs.add(arr)
    for s in map:
        if s not in arrs:
            start = s
    q = deque([start])
    res = []
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in map:
                q.append(map[curr])
            res.append(curr)
    return res

# codepath solution
from collections import defaultdict
def find_itinerary(boarding_passes):
    map = defaultdict(list)
    for dept, arr in boarding_passes:
        map[dept].append(arr)
    for s in map:
        map[s].sort(reverse=True)
    res = []
    def dfs(state):
        while map[state]:
            next_flight = map[state].pop()
            dfs(next_flight)
        res.append(state)
    start = boarding_passes[0][0]
    dfs(start)
    return res[::-1]

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))


# Problem 7
def counting_flights(flights, i, j):
    q = deque([i])
    total_flights = 0
    visited = set()
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == j:
                return total_flights
            for f in range(len(flights[curr])):
                if flights[curr][f] == 1 and f not in visited:
                    visited.add(f)
                    q.append(f)
        total_flights += 1
    return -1
        

flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))

# Problem 8

# Plan
# dfs
# use a visited set to prevent infinite calls
# iterate over each airport (airport is the index if each row) and only 
#   increse no of regions if its not yet visited
# run a dfs on the airport while adding its connected airport to visited
def num_airline_regions(is_connected):
    n = len(is_connected)
    regions = 0
    visited = set()
    def dfs(airport):
        for neighbour in range(len(is_connected[airport])):
            if is_connected[airport][neighbour] == 1 and neighbour not in visited:
                visited.add(neighbour)
                dfs(neighbour)

    for airport in range(n):
        if airport not in visited:
            dfs(airport)
            visited.add(airport)
            regions += 1
    return regions
is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 