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