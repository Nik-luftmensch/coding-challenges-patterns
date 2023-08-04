#  Given the word count is equal we can then only use the second for
# loop to iterate over the second word and try to find the value in the lookup
# or else we might have to run the loop like we did in fc.py check it once

w1,w2 = "aza","zaa"

def Anagram(w1,w2):
    if (len(w1) != len(w2)):
        return False

    lookup = {}

    for i in w1:
        lookup[i] = (lookup.get(i,0))+1
    
    for letter in w2:
        if (letter not in lookup):
            return False
        else:
            lookup[letter] -= 1
    
    return True

a = Anagram(w1, w2)
print(a)