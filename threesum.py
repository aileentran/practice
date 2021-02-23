"""
Leetcode - 15. 3Sum

input: list of nums
output: list of unique triplets that sum to 0

Notes:
no duplicate triplets
can reuse some numbers

Thoughts
empty results list

use a triple nested loop to go through the list

return results

think of another solution that's less than O^3 time
"""

def threeSum(nums):
    if len(nums) <= 2:
        return []

    nums.sort()
    triplets = set()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                # print(nums[i], nums[j], nums[k])
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = (nums[i], nums[j], nums[k])
                    triplets.add(triplet)

    triplets = list(triplets)
    for t, triplet in enumerate(triplets):
        triplets[t] = list(triplet)

    return triplets

nums1 = [-1,0,1,2,-1,-4] #[[-1,-1,2],[-1,0,1]]
nums2 = [] #[]
nums3 = [0] #[]

print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
