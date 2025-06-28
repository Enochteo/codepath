def reverse(lst):
    if not lst:
        return []
    if len(lst) == 1:
        return lst
    first = [lst[0]]
    second = reverse(lst[1:])
    return second + first

print(reverse([1,2,3,4]))