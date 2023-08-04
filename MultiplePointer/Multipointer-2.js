// Two Sum but since number is not sorted doing this is better, if it wasa sorted then doing two pointer  will make sense
function twoSum(nums, target) {
    let dict = {}
    for (let i= 0; i<nums.length; i++){
        let diff = target - nums[i]
        if(diff in dict){
            return([i,dict[diff]])
        }
        else{
            dict[nums[i]] = i
        }
    }
    return false
}

console.log(twoSum([1,2,4,5,3],7))
