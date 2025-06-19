def rearrange_guests(guests):
    # does not work for all cases
    l = 0
    r = 1
    while l < len(guests) and r < len(guests):
        if guests[l] * guests[r] < 0:
            l += 1
            r += 1
        else:
            if l < r:
                while guests[l] * guests[r] > 0:
                    l += 1
                guests[l], guests[r] = guests[r], guests[l]
                #r += 1
            else:
                while guests[r] * guests[l] > 0:
                    r += 1
                guests[r], guests[l] = guests[l], guests[r]
    return guests
print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 
print(rearrange_guests([1,-1,-2,3,5,7,-4])) 
print("Better - v")
def rearrange_guests(guests):
    for i in range(len(guests)):
        if (i%2 == 0) and guests[i] > 0:
            continue
        elif (i%2 != 0) and guests[i] < 0:
            continue
        j = i + 1
        while j<=len(guests):
            if (i%2 == 0 and guests[j]>0) or (i%2 != 0 and guests[j]<0):
                break
            j += 1
            if j == len(guests):
                break
        temp = guests[j]
        for k in range(j, i, -1):
            guests[k] = guests[k-1]
        guests[i] = temp
    return guests
print(rearrange_guests([3,1,-2,-5,2,-4]))
print(rearrange_guests([-1, 1]))
print(rearrange_guests([1,-1,-2,3,5,7,-4])) 
