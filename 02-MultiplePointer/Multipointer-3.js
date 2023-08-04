// Count Unique Values sorted hai 
function uv(a){
    let dict = {}
    let u = 0
    for(val of a){
        dict[val] ? (dict[val] += 1 ) : (dict[val] = 1) && u ++
    }
    return u
}
console.log(uv([-1,-2,-2,0,1,1,1,2,3,4,5,6,7]))