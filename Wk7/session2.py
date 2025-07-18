# def check_stock(inventory, part_id):
#     def find_item(left, right):
#         if left > right:
#             return False
#         mid = (left + right)  // 2
        
#         if inventory[mid] == part_id:
#             return True
#         elif inventory[mid] > part_id:
#             return find_item(left, mid-1)
#         else:
#             return find_item(mid+1, right)
        
#     return find_item(0, len(inventory)-1)
        
# print(check_stock([1, 2, 5, 12, 20], 20))
# print(check_stock([1, 2, 5, 12, 20], 100))
# # Plan
# # binary search
# # recursive
# # helper function - parameters # l, r,
# #   if l > r - base case 
# #   find mid
# #   if mid is part_id
# #       return True
# #   if part id is less than mis
# #       recursively left
# #   if greater
# #       recursively call right
# #   return False 


# # Problem 2 - Iteratively
# def check_stock(inventory, part_id):
#     l, r = 0, len(inventory)-1
#     while l<=r:
#         mid = (l+r)//2
#         if inventory[mid] == part_id:
#             return True
#         elif inventory[mid] < part_id:
#             l = mid + 1
#         else:
#             r = mid -1
#     return False

# print(check_stock([1, 2, 5, 20, 12], 20))
# print(check_stock([1, 2, 5, 20, 12], 100))

#[5,7,7,8,8,10], 8
# Problem 3
def find_frequency_positions(transmissions, target_code):
    
    def helper_first(l, r):
        last_elem = r
        if l >= r:
            return last_elem
        mid = (l+r)//2
        if transmissions[mid] == target_code:
            return helper_first(l, mid)
        elif transmissions[mid] > target_code:
            return helper_first(l, mid-1)
        else:
            return helper_first(mid+1, r)
    def helper_last(l,r):
        first_elem = l
        if l >= r:
            return first_elem
        mid = (l+r)//2
        if transmissions[mid] == target_code:
            return helper_last(mid, r)
        elif transmissions[mid] > target_code:
            return helper_last(l, mid-1)
        else:
            return helper_last(mid+1, r)
        
    begin = helper_first(0, len(transmissions))
    end = helper_last(0, len(transmissions))
    if begin == end and transmissions[begin] != target_code:
        return (-1, -1)
        

    return (begin, end)

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
print('iterative')
def find_frequency_iterative(transmissions, target_code):

    # Edge casesm in case that the transmissions array either only have one or zero length
    if len(transmissions) == 0:
        return (-1, -1)
    elif len(transmissions) == 1 and transmissions[0] == target_code:
        return (0, 0)
    
    #  Setting up l an r, along with mid
    l, r = 0, len(transmissions) - 1

    mid = (l + r) // 2
    
    # Finding the mid using binary search
    while l < r and transmissions[mid] != target_code:

        if transmissions[mid] < target_code:
            l = mid + 1
        elif transmissions[mid] > target_code:
            r = mid - 1
        
        mid = (l + r) // 2

    # If we already checked the whole array and there mid is still not equal to target code, then the code does not exist
    if l >= r and transmissions[mid] != target_code:
        return (-1, -1)
    
    
    temp = mid - 1

    #  If mid - 1 is not the target_code, then the mid index is the smallest index of the code
    if transmissions[temp] != target_code:
        l = mid
    else:
        
        while l != temp:
            
            middle = (l + temp) // 2
            
            #  If transmission[middle] is equal to target_code, then it is safe to assume that everything on the right side of middle is the target code
            # Then we can just assign temp to the middle
            # Otherwise, we can just assign l with middle
            if transmissions[middle] == target_code:
                temp = middle
            else: 
                l = middle

    temp = mid + 1

    #  If mid + 1 is not the target_code, then the mid index is the highest index of the code
    if transmissions[temp] != target_code:
        r = mid
    else:
        
        # Will continuously update until r == temp
        while r != temp:
            
            # Get the middle index between r and temp
            middle = (r + temp) // 2
            
            #  If transmission[middle] is equal to target_code, then it is safe to assume that everything on the left side of middle is the target code
            # Then we can just assign temp to the middle
            # Otherwise, we can just assign r with middle
            if transmissions[middle] == target_code:
                temp = middle
            else: 
                r = middle
    
    return (l,r)

print(find_frequency_iterative([5,7,7,8,8,10], 8))
print(find_frequency_iterative([5,7,7,8,8,10], 6))
print(find_frequency_iterative([], 0))

# [5,5,5,5]
#  l  m  r
# binary search
# we use binary search to find the number,
# when we find the mid m== target_code
    # curively search the left part - beginning
    # recursively call the right - end
# return (begining, end)


# [5,5,5,5]
#  l  m  r
# binary search
# we use binary search to find the number,
# when we find the mid m== target_code
    # curively search the left part - beginning
    # recursively call the right - end
# return (begining, end)
