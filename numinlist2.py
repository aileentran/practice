"""
input: list of nums, target
output: boolean - true if target is in list, false otherwise

Thoughts
brute force method
go through list as is and see if num == target

binary search
sort the list
floor set to 1 below actual floor (-1)
ceil set 1 above actual ceil (len(nums))

while floor + 1 < ceil - gap of at least 1
find center idx in context of floor
find value of center index

if target == center -> return true
if target < center, bring ceil down to center idx
if target > center, bring floor to center idx

outside loop, return false
"""

def num_in_list(nums, target):
    nums.sort()
    floor = -1
    ceil = len(nums)

    while floor + 1 < ceil:
        half = (ceil - floor) // 2
        center = floor + half
        
        if target == nums[center]:
            return True
        if target < nums[center]:
            ceil = center
        elif target > nums[center]:
            floor = center

    return False

list1 = [9, 5, 3, 1, 4]
num1 = 3
# True
list2 = []
num2 = 3
# False
list3 = [1, 2, 3, 4]
num3 = 4
# True
list4 = [1, 2, 3, 4]
num4 = 9
# False

print(num_in_list(list1, num1))
print(num_in_list(list2, num2))
print(num_in_list(list3, num3))
print(num_in_list(list4, num4))
