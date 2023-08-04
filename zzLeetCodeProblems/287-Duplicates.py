# FloydsCycle
# Without Modifying the Array or using any other extra memory

nums = [4,1,3,3,2]

def Duplicates(nums):
    slow,fast = 0,0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

a = Duplicates(nums)
print(a)