"""
Grokking Ch. 4

4.2 WRite a recursive function to count the number of items in a list
input: list of.. things
output: num - number of items in the list

Thoughts
base case: empty list, return 0

return 1 + func(list[1:])
"""

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

list1 = ['a', 1, 'C'] #3
list2 = [] #0

print(count(list1))
print(count(list2))
