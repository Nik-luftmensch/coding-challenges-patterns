# numbers are not sorted and a tweak that two number that is equal to a sum 

nums = [5,4,-3,2,1,1]
number = 6

def TwoSum(nums,number):
    dict = {}
    for i in nums:
        diff = number-i
        if diff in dict:
            return [dict[diff],i]
        else:
            dict[diff] = i



a = TwoSum(nums,number)
print(a)