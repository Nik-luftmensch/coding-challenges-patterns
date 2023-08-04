//Sliding window find max sum of a certain digit Naive

function SlidingWindow(a,d) {
    if (d > a.length){
        return null
    }
    var max = -Infinity
    for(let i=0;i<a.length-d +1;i++){
        let temp = 0
        for(let j=0;j<d;j++){
            temp += a[i+j]
        }
        if(temp > max){
            max = temp
        }
        
    }
    return max
}
console.log(SlidingWindow([5,6,2,1,3,4,3,2,3,17,4],2))