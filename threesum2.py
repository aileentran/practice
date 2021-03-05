"""
Leetcode - 15. 3Sum

input: list of nums
output: list of unique triplets that each sum to 0

Thoughts
if the nums list < 3, return []

make empty results list
sort the nums list

loop through the list
look at the first item
check to make sure we're not looking at repeated nums!
if were past the first num, check to make sure current num != to prev num

nested loop
two pointers, one at beginning and one at end
make sure it's not the same as "prev" num too!
if the sum of 3 nums > 0, move right pointer left
if sum of 3 nums < 0, move left pointer to the right
else append to empty results list
"""

def threeSum(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    triplets = []
    
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:

            # doesn't handle more than 2 repeats.. = need a loop
            # if left > i + 1 and nums[left - 1] == nums[left]:
            #     left += 1
            # if right < len(nums) - 2 and nums[right + 1] == nums[right]:
            #     right -= 1

            sum = num + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                triplets.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return triplets

nums1 = [-1,0,1,2,-1,-4, -1] #[[-1,-1,2],[-1,0,1]]
nums2 = [] #[]
nums3 = [0] #[]
nums4 = [0,0,0,0] #[[0, 0, 0]]

print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
print(threeSum(nums4))
