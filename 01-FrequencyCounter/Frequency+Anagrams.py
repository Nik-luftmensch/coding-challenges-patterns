list1 = [1,2,3,2]
list2 = [9,1,4,4]

def same(list1, list2):
    if len(list1) != len(list2):
        return False
    lookup= {}

    for i in list2:
        lookup[i] = (lookup.get(i,0)) +1
    
    for i in list1:
        if(i**2 not in lookup):
            return False
        else:
            lookup[i**2] -= 1
    return True

a = same(list1, list2)
print(a)