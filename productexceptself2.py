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
    products = []
    left = [0] * len(nums)
    right = [0] * len(nums)

    left[0] = 1
    for i in range(1, len(left)):
        left[i] = left[i - 1] * nums[i - 1]

    right[len(right) - 1] = 1
    for i in reversed(range(len(right) - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(len(nums)):
        products.append(left[i] * right[i])

    return products

nums = [1,2,3,4] #[24,12,8,6]

print(productExceptSelf(nums))
