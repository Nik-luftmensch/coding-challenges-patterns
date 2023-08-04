//Sliding window find max sum of a certain digit Naive


function  SlidingWindow(a,d) {
    let tempSum = 0
    let maxSum = 0

    for (let i =0;i<d;i++){
        maxSum += a[i]
    }

    tempSum = maxSum

    for(let i =d;i<a.length;i++)
        {
            tempSum = tempSum - a[i-d]  + a[i]
            maxSum = Math.max(tempSum,maxSum)
        }
    return maxSum
}


console.log(SlidingWindow([5,6,16,2,1,3,4,3,2,3,17,4],2))


