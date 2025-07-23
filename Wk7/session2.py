# Problem 1
print("Problem 1")
def check_stock(inventory, part_id):
    def find_item(left, right):
        if left > right:
            return False
        mid = (left + right)  // 2
        
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] > part_id:
            return find_item(left, mid-1)
        else:
            return find_item(mid+1, right)
        
    return find_item(0, len(inventory)-1)
        
print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))
# Plan
# binary search
# recursive
# helper function - parameters # l, r,
#   if l > r - base case 
#   find mid
#   if mid is part_id
#       return True
#   if part id is less than mis
#       recursively left
#   if greater
#       recursively call right
#   return False 


# Problem 1 - Iteratively
print("Problem 1 - Iteratively")
def check_stock(inventory, part_id):
    l, r = 0, len(inventory)-1
    while l<=r:
        mid = (l+r)//2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            l = mid + 1
        else:
            r = mid -1
    return False

print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100))

[5,7,7,8,8,10], 8
# Problem 3
print("Problem 3")
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


def find_frequency_recursive(transmissions, target_code):
    if not transmissions:
        return (-1, -1)
    def helper1(l,r):
        if l > r:
            return -1
        mid = (l + r)//2
        if transmissions[mid] == target_code:
            if mid == 0 or transmissions[mid-1] < target_code:
                return mid
            else:
                return helper1(l, mid-1)
        elif transmissions[mid] < target_code:
            return helper1(mid+1, r)
        else:
            return helper1(l, mid-1)
    def helper2(l,r):
        if l > r:
            return -1
        mid = (l + r)//2
        if transmissions[mid] == target_code:
            if mid == len(transmissions) - 1 or transmissions[mid + 1] > target_code:
                return mid
            return helper2(mid+1, r)
        elif transmissions[mid] < target_code:
            return helper2(mid+1, r)
        else:
            return helper2(l, mid-1)
    tups = (helper1(0, len(transmissions)-1), helper2(0, len(transmissions)-1))
    return tups

print('recursive')
print(find_frequency_recursive([5,7,7,8,8,10], 8))
print(find_frequency_recursive([5,7,7,8,8,10], 6))
print(find_frequency_recursive([], 0))

# Problem 4

# binary search problem
#PLAN
# The idea is that if mid is greater we want to search the left
# if mid is lesser let binary search cover - search right
# we return if mid is greater and mid == l
print("Problem 4")
def next_greatest_letter(letters, target):
    def helper(l, r, candidate):
        if l > r:
            return candidate if candidate else letters[0]
        #print(letters[mid])
        mid = (l+r)//2
        if letters[mid] >= target:
            candidate = letters[mid]
            return helper(l, mid-1, candidate)
        if letters[mid] < target:
            return helper(mid+1, r, candidate)
    return helper(0, len(letters)-1, None)

# letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

# print(next_greatest_letter(letters, 'a'))
# print(next_greatest_letter(letters, 'd'))
# print(next_greatest_letter(letters, 'y'))

letters = [1,2,4,6,8,9,11,12]
print(next_greatest_letter(letters, 3))

# Problem 5
print("Problem 5")
# sliding window
def find_closest_planets(planets, target_distance, k):
    l = 0
    r = len(planets) - 1
    while r - l >= k:
        if abs(planets[l] - target_distance) > abs(planets[r] - target_distance):
            l += 1
        else:
            r -= 1
    return planets[l:r+1]

planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]
planets3 = [1,2,3,4,5,6,7,8,9]

print(find_closest_planets(planets1, 350, 3))
print(find_closest_planets(planets2, 25, 2))
print(find_closest_planets(planets3, 9, 4))

# two pointer - sliding window
# the window to initially be the array
# compress the window till window length = (target distance) using greedy:
    # if abs(arr[l] - target distance) > abs(arr[r]-target distance):
    #   move l
    # else
    #   move r
    # 
# return the list slice from l to r+1 

# Time comp. -> O(N - K) avg O(N)
# space -> O(1) not counting return

# binary search solution:
# find the index of the closest or target distance
#  create a closest list
# while closestlist.length != k
    # expand from closest with two pointers based on which is closer
    # append to closest list
# return closest list
print("BINARY SEARCH")
def find_closest_planet2(planets, target_distance, k):
    def binary_search(l, r):
        if l >= r:
            return l
        mid = (l+r)//2
        if planets[mid] > target_distance:
            return binary_search(l, mid)
        else:
            return binary_search(mid + 1, r) 
    
    closest_index = binary_search(0, len(planets)-1)
    l = r = closest_index
    closest_list = []
    while len(closest_list) != k:
        if l < 0:
            closest_list.append(planets[r])
            r += 1
        elif r > len(planets) - 1:
            closest_list.append(planets[l])
            l -= 1 
        elif abs(planets[l] - target_distance) > abs(planets[r] - target_distance):
            closest_list.append(planets[l])
            l -= 1
        else:
            closest_list.append(planets[r])
            r -= 1
    return sorted(closest_list)
        
planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]
planets3 = [1,2,3,4,5,6,7,8,9]

print(find_closest_planet2(planets1, 350, 3))
print(find_closest_planet2(planets2, 25, 2))
print(find_closest_planet2(planets3, 9, 4))