"""
input: list of nums, num
output: boolean - true if num in list, false otherwise

Thoughts
brute force method
loop through list to find num

binary search
sort list of nums
floor variable set to 0 idx
ceiling variable set to end of list

while floor < ceil
check if num is ==, <, > middle number (whole int)
if num ==, return true
if num <, bring ceil to middle
if num >, bring floor to middle

outside loop, return false
"""

def num_in_list(list, num):
    list.sort()
    # floor and ceil need to be OUTSIDE of list to INCLUDE list
    floor = -1
    ceil = len(list)

    while floor + 1 < ceil:
        distance = (ceil - floor) // 2
        middle = floor + distance # need to consider that floor is changing
        guess = list[middle]
        
        print(guess, '==?', num)
        if num == guess:
            return True
        if num < guess:
            ceil = middle
        elif num > guess:
            floor = middle

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
