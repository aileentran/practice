"""
Leetcode - 238. Product of Array Except Self

input: list of nums
output: list of nums - each ele is product of all other nums except itself

Notes: do it on O(n) time and without dividing

Thoughts:
make empty results list
create lists for products of left and right of element - loop separately
loop through input and append products of left and right into results
return result

left i - 1, right i + 1
"""
def productExceptSelf(nums):
    return

nums = [1,2,3,4] #[24,12,8,6]

print(productExceptSelf(nums))
