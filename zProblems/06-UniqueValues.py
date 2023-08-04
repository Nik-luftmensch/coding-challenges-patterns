# Count the number of Unique Values without adding a new data set
nums = [-1,-1,-2,0,1,1,1,2,3,4,5,6,7,7,7,19,20]
def UniqueNumber(nums):
    i,j = 0,1
    while j < len(nums):
        if nums[i] != nums[j]:
            i+= 1
            nums[i] = nums[j]
        j +=1
    return i+1
    
a = UniqueNumber(nums)
print(a)
