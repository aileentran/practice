"""
HackerRank: A Very Big Sum

input: an array of nums
output: summed num
"""

def aVeryBigSum(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum

big_nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(big_nums))
