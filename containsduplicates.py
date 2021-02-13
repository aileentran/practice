"""
Leetcode - 217. Contains Duplicate

input: list of nums
output: true if at least 1 duplicate, false otherwise

thoughts
create a set
compare length to input list, if diff return true, false otherwise
"""
def containsDuplicate(nums):
    unique = set(nums)

    print(nums)
    print(unique)

    if len(unique) != len(nums):
        return True

    return False

nums1 = [1,2,3,1] #true
nums2 = [1,2,3,4] #false
nums3 = [1,1,1,3,3,4,3,2,4,2] #true

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
