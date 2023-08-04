//Find the number of Pairs whose sum is 0 and sorted
// Ask Questions such as is it sorted, only one pair is 0 or nore than one pair
function multiplePointer(a) {
    let left = 0 
    let right = a.length - 1
    while(left < right){
        let sum = a[left] + a[right]
        if(sum === 0){
           return([a[left],a[right]])
        }
        else if(sum > 0){
            right--
        }
        else{
            left++
        }
    }
    return undefined
}

multiplePointer([-4,-3,-2,-1,0,1,2,5,10])