"""
Hackerrank - Greedy Algorithm: Minimum Absolute Difference in an Array
"""

# Thoughts
# make empty minimum difference
# create all potential pairs (only let in ones we haven't seen)
#  loop through and make potential pairs
# loop through potential pairs and take absolute differnce
# if less than minimum difference, set to min
# outside loop, return min
# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    minimum = None
    pairs = set()

    i = 0
    while i < len(arr) - 1:
        num1 = arr[i]
        k = 1
        while k < len(arr):
            num2 = arr[k]
            if num1 != num2:
                pair = (num1, num2)
            if pair not in pairs:
                pairs.add(pair)
            k += 1
        i += 1
    
    for pair in pairs:
        num1, num2 = pair
        diff = abs(num1 -  num2)
        if minimum == None:
            minimum = diff
        elif diff < minimum:
            minimum = diff
    return minimum