"""
Leetcode - 220. Contains Duplicate III

input: list of nums, k(idx), t(value)
output: boolean
True if diff of vals <= t and diff of idx <= k

Thoughts
create an empty dictionary
key - num, val - the latest index

loop through nums using range
nested loop to check value in dictionary
if the value is within num +- t and both idxs are within k range, return true 

outside loop return false
"""

def containsNearbyAlmostDuplicate(nums, k, t):
    print(nums)
    print('k index', k)
    print('t value', t)
    dict = {}
    for i, num in enumerate(nums):
        print('i', i)
        print('num', num)
        print(dict)
        for val in dict:
            if num - t <= val <= num + t and abs(dict[val] - i) <= k:
                return True
        dict[num] = i
        # print(dict)
        print('\n')
    return False

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

nums4 = [8,7,15,1,6,1,9,15]
k4 = 1
t4 = 3
# True

# print(containsNearbyAlmostDuplicate(nums1, k1, t1))
# print(containsNearbyAlmostDuplicate(nums2, k2, t2))
print(containsNearbyAlmostDuplicate(nums3, k3, t3))
# print(containsNearbyAlmostDuplicate(nums4, k4, t4))
