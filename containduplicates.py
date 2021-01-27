"""
Leetcode - Contains Duplicate

input: list of numbers
output: boolean - true if has duplicates, false otherwise

sorting the nums
loop through nums looking at pairs (account for index range)
once there's a match, return true

outside loop, return false
"""
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        num1 = nums[i]
        num2 = nums[i + 1]
        if num1 == num2:
            return True
    return False

nums1 = [1,2,3,1] #true
nums2 = [1,2,3,4] #false
nums3 = [1,1,1,3,3,4,3,2,4,2] #true

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
