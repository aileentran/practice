"""
Leetcode - 219. Contains Duplicate II

input: list of nums, k (int)
output: boolean - True if duplicates and abs difference of indices < k
"""
def containsNearbyDuplicate(nums, k):
    return

nums1 = [1,2,3,1]
k1 = 3
# True

nums2 = [1,0,1,1]
k2 = 1
# True

nums3 = [1,2,3,1,2,3]
k3 = 2
# False

print(containsNearbyDuplicate(nums1, k1))
print(containsNearbyDuplicate(nums2, k2))
print(containsNearbyDuplicate(nums3, k3))
