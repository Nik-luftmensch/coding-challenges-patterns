// Count Unique Values sorted hai 

function uv(a){
    let i = 0
     for(let j=1;j<a.length;j++){
       if(a[i]!==a[j]){
           i++
           a[i] = a[j]
       }
     }
     return i+1
 }
 console.log(uv([-1,-1,-2,0,1,1,1,2,3,4,5,6,7,7]))
 