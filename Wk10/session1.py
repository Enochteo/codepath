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

from collections import defaultdict

def find_itinerary(boarding_passes):
    # Step 1: Build the graph (adjacency list)
    flights = defaultdict(list)
    
    # Create adjacency list where each airport has a list of destinations
    for departure, arrival in boarding_passes:
        flights[departure].append(arrival)
    
    # Step 2: Sort the destinations for each departure airport (optional)
    # This ensures we visit in lexicographical order if required
    for airport in flights:
        flights[airport].sort(reverse=True)

    # Step 3: Perform DFS and build the itinerary
    result = []
    
    def dfs(airport):
        # Visit all the destinations for the current airport
        while flights[airport]:
            next_flight = flights[airport].pop()
            dfs(next_flight)
        # Once all destinations are visited, add the airport to the result
        result.append(airport)

    # Step 4: Start DFS from the starting airport
    start_airport = boarding_passes[0][0]  # Assumption: we start from the first departure
    dfs(start_airport)
    
    # Step 5: The itinerary will be in reverse order due to DFS, so reverse the result
    return result[::-1]
    
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
