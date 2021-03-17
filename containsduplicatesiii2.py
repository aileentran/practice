"""
Leetcode - 220. Contains Duplicate III

input: list of nums, k(idx), t(value)
output: boolean
True if diff of vals <= t and diff of idx <= k
"""

def containsNearbyAlmostDuplicate(nums, k, t):
    return

nums1 = [1,2,3,1]
k1 = 3
t1 = 0
# True
nums2 = [1,0,1,1]
k2 = 1
t2 = 2
# True
nums3 = [1,5,9,1,5,9]
k3 = 2
t3 = 3
# False

print(containsNearbyAlmostDuplicate(nums1, k1, t1))
print(containsNearbyAlmostDuplicate(nums2, k2, t2))
print(containsNearbyAlmostDuplicate(nums3, k3, t3))
