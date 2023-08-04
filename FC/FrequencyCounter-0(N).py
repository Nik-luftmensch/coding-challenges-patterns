list1 = [1,2,3,2]
list2 = [9,1,4,4]

def same(list1, list2):
    if len(list1) != len(list2):
        return False
    fc1= {}
    fc2= {}
    
    for i in list1:
        fc1[i] = (fc1.get(i,0)) + 1
    for i in list2:
        fc2[i] = (fc2.get(i,0)) +1
    for key in fc1:
        key2 = key**2
        if (key2 not in fc2) and (fc1[key] != fc2.get(key2)):
            return False
    return True
a = same(list1, list2)
print(a)