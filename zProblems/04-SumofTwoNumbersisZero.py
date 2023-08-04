#Sum of Two Numbers is zero when the number is sorted
nums = [-4,-3,-2,-1,0,1,2,5,10]

def TwoSum(nums):
    l,r = 0, len(nums)-1
    while l < r:
        sum = nums[l] + nums[r]
        if sum < 0:
            l += 1
        elif sum>0:
            r -= 1
        else:
            return [nums[l],nums[r]]


a = TwoSum(nums)
print(a)