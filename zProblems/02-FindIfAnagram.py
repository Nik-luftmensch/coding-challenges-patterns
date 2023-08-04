w1,w2 = "aza","zaa"

def Anagrams(w1,w2):
    lookup = {}

    if len(w1) != len(w2):
        return False
    
    for i in w1:
        lookup[i] = (lookup.get(i,0))+1

    for j in w2:
        if j not in lookup:
            return False
        else:
            lookup[j] -= 1
    return True

a = Anagrams(w1,w2)
print(a)