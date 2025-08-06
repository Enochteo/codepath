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
