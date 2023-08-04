function same(a,b){
    if(a.length !== b.length){
        return false
}
    let fc1 = {}
    for (let val of b){
        fc1[val] ? fc1[val] +=1 : fc1[val] = 1
    }
    console.log(fc1)
    for (let val of a){
        if(!fc1[val**2]){
            return false
        }
        else{
            fc1[val**2] -= 1
        }
    }
    return true
}
console.log(same([1,2,3,4,4,5],[1,4,9,25,16,16]))