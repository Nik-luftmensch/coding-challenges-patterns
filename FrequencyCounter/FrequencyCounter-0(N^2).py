list1 = [1,2,3,2]
list2 = [9,1,4,4]

def same(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in list1:
        squaredNumber = i ** 2
        if squaredNumber not in list2:
            return False
        else:
            list2.remove(squaredNumber)
    return True

a = same(list1, list2)
print(a)
