list1 = [1,2,3,2]
list2 = [9,1,4,4]

def SquaredNumbers(list1,list2):
    fc1 = {}
    fc2 = {}
    if len(list1) != len(list2):
        return False    
    
    for i in list1:
        fc1[i] = (fc1.get(i,0))+1
    for j in list2:
        fc2[j] = (fc1.get(j,0))+1
    
    for key1 in fc1:
        key2 = key1**2
        if (key2 not in fc2) and (fc1[key1] != fc2.get(key2)):
            return False
    return True





a = SquaredNumbers(list1,list2)
print(a)