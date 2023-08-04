nums = [1,2,3,4]

# def Duplicates(nums):
#     dict = {}
#     for i in nums:
#         if i in dict:
#             return False
#         else:
#             dict[i] = i
#     return True


def Duplicates(nums):
    if len(nums) != len(set(nums)):
        return False
    return True


a = Duplicates(nums)
print(a)