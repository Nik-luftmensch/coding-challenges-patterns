function anagram(w1,w2){
    if (w1.length !== w2.length){
        return false
    }
    const lookup = {}
    for(let i = 0; i<w1.length;i++){
        let letter = w1[i]
        lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1
    }
    for(let i = 0; i<w2.length;i++){
        let letter = w2[i]
        if(!lookup[letter]){
            return false
        }
        else {
            lookup[letter] -=1
        }
    }
    return true
}

console.log(anagram("aza","zaa"))