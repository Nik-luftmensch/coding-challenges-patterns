function same(a,b){
    if(a.length !== b.length){
        return false
}
    let fc1 = {}
    let fc2 = {}
    for (let val of a){
        fc1[val] = (fc1[val]||0)+1
    }
    for (let val of b){
        fc2[val] = (fc2[val]||0)+1
    }
    for(let key in fc1){
        key2 = key**2
        if(!(key2 in fc2) && fc1[key] !== fc2[key2]){
            return false
        }
    }

    return true
}
console.log(same([1,2,3,4,4,5],[1,4,9,25,16,16]))