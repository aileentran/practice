"""
Practicing recursion w/Fibonacci

input: num - how many of the sequence to output
output: list of Fibonacci nums

notes:
starts with 0 and 1
curr num is the sum of 2 previous nums
"""

def fibonacci(num):
    if num == 0 or num == 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(1))
print(fibonacci(9))
