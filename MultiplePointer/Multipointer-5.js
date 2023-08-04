// Count Unique Values sorted hai 

function uv(a){
    i = 0
    j = i+1
    u = 1
    while (j<a.length){
        if(a[i] == a[j]){
            j++
        }
        else{
            i = j
            u++
            j++

        }
    }
    return u
}

console.log(uv([-1,-1,-2,-2,0,1,1,1,2,3,4,5,6,7,7]))