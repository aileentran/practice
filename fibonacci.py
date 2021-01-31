"""
Practicing recursion w/Fibonacci

input: num - how many of the sequence to output
output: list of Fibonacci nums

notes:
starts with 0 and 1
curr num is the sum of 2 previous nums
"""

def fibonacci(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)

# print(fib(1))
print(fibonacci(9))
