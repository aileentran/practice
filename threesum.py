"""
Leetcode - 15. 3Sum

input: list of nums
output: list of unique triplets that sum to 0

Notes:
no duplicate triplets
can reuse some numbers

Thoughts

brute force solution:
- empty results list
- use a triple nested loop to go through the list
- return results
--> eventually timed out with very large input

Ideas
- eliminate duplicates in list
- stop looping once hit positive numbers bc cannot sum to 0
- Review two sum II
"""

def threeSum(nums):
    if len(nums) <= 2:
        return []

    nums.sort()
    triplets = []

    for n, num in enumerate(nums):
        if n > 0 and num == nums[n - 1]:
            continue
        left = n + 1
        right = len(nums) - 1
        while left < right:
            sum = num + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                triplets.append([num, nums[left], nums[right]])
                # need to update one pointer and earlier conditions will update other pointer
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return triplets

nums1 = [-1,0,1,2,-1,-4] #[[-1,-1,2],[-1,0,1]]
nums2 = [] #[]
nums3 = [0] #[]
nums4 = [0,0,0,0] #[]

print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
print(threeSum(nums4))
