"""
input: number - how many coins i can use
output: set of numbers - total amount of money! based on coin combos

# NOTE:
pennies (1) and dimes (10)

Thoughts
brute force - make every combination possible - maybe long long run time
result variable - set
list of values for each --> pennies --> list of ones length of num_coins
loop range num_coins inclusive
sum the values in list and add to set
start replacing values with dimes

recursion + memoize using dynamic programming - save previous calcs in dictionary
"""

# class PinchingPennies():
#     def __init__(self):
#         self.memo = {}

def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """
    result = set()
    change = [1] * num_coins # start w/all pennies

    for i in range(num_coins):
        result.add(sum(change))
        change[i] = 10

    result.add(num_coins * 10)
    return result

# runtime: O(n^2) - for loop AND sum()
# space complexity: O(n)



print(coins(1) == {1, 10})
print(coins(2) == {2, 11, 20})
print(coins(3) == {3, 12, 21, 30})
print(coins(4) == {4, 13, 22, 31, 40})
print(coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100})
