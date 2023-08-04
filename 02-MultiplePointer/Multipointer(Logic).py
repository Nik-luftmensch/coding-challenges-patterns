numList = [-1,-1,-2,-2,0,1,1,1,2,3,4,5,6,7,7]

def UniqueValues(a):
    i = 0
    for j in range(1,len(a)):
        if (a[i] != a[j]):
            print(a[i],a[j])
            i += 1
            a[i] = a[j]
            print(a)
    return i+1

a = UniqueValues(numList)
print(a)